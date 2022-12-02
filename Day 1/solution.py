def aoc_day1(a):

  with open(a) as f:
    contents = f.read()

  carried_calories = [sum([int(calorie) for calorie in content.split("\n")]) 
                for content in contents[:-2].split("\n\n")]
  
  max_calorie = max(carried_calories)

  carried_calories.sort(reverse=True)

  top3 = carried_calories[0]+carried_calories[1]+carried_calories[2]

  return "max calorie: {} sum of top 3 calories: {}".format(max_calorie,top3)

print(aoc_day1('input.txt'))
