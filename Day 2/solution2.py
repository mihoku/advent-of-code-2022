#A=Rock,B=Paper,C=Scissors
#X=Lose,Y=Draw,Z=Win

def aoc_day2_partB(a):

  with open(a) as f:
    text = f.read()

  command= {'X':'lose','Y':'draw','Z':'win'}

  opponent_choice = {'A': {'win':'B','draw':'A','lose':'C'}, 
                     'B': {'win':'C','draw':'B','lose':'A'}, 
                     'C':{'win':'A','draw':'C','lose':'B'}}

  scoring = {'win':6,'draw':3,'lose':0}
  choice_scoring = {'A':1,'B':2,'C':3}

  total_score = 0

  for entry in text[:-1].replace(" ","").split("\n"):
    total_score+=choice_scoring[opponent_choice[entry[0]][command[entry[1]]]]+scoring[command[entry[1]]]
  
  return total_score

print(aoc_day2_partB("day2-input.txt"))
