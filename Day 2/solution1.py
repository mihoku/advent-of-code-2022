#A=Rock,B=Paper,C=Scissors
#X=Rock,Y=Paper,Z=Scissors

def aoc_day2_partA(a):

  with open(a) as f:
    text = f.read()

  game_ruling = {'A': {'Y':'win','X':'draw','Z':'lose'}, 
                 'B': {'Z':'win','Y':'draw','X':'lose'}, 
                 'C':{'X':'win','Z':'draw','Y':'lose'}}

  scoring = {'win':6,'draw':3,'lose':0}
  choice_scoring = {'X':1,'Y':2,'Z':3}

  total_score = 0

  for entry in text[:-1].replace(" ","").split("\n"):
    total_score += choice_scoring[entry[1]] + scoring[game_ruling[entry[0]][entry[1]]]

  return total_score

print(aoc_day2_partA("day2-input.txt"))
