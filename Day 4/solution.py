def DataRead(a):
  with open(a) as x:
    contents = x.read()
    return contents

def OverlapTest(b):
  assignments = b.split(',')
  if int(assignments[0].split('-')[0]) >= int(assignments[1].split('-')[0]) and int(assignments[0].split('-')[1]) <= int(assignments[1].split('-')[1]):
    return True
  elif int(assignments[1].split('-')[0]) >= int(assignments[0].split('-')[0]) and int(assignments[1].split('-')[1]) <= int(assignments[0].split('-')[1]):
    return True
  else: 
    return False

def OverlapTestRefined(c):
  assignments = c.split(',')
  if int(assignments[0].split('-')[0]) >= int(assignments[1].split('-')[0]) and int(assignments[0].split('-')[0]) <= int(assignments[1].split('-')[1]):
    return True
  elif int(assignments[0].split('-')[1]) >= int(assignments[1].split('-')[0]) and int(assignments[0].split('-')[1]) <= int(assignments[1].split('-')[1]):
    return True
  elif int(assignments[1].split('-')[0]) >= int(assignments[0].split('-')[0]) and int(assignments[1].split('-')[0]) <= int(assignments[0].split('-')[1]):
    return True
  elif int(assignments[1].split('-')[1]) >= int(assignments[0].split('-')[0]) and int(assignments[1].split('-')[1]) <= int(assignments[0].split('-')[1]):
    return True
  else: 
    return False

def aoc_day4_partA(x):
  assignment_list = DataRead(x)[:-1].split('\n')
  overlap_assignment = sum([1 if OverlapTest(i)  else 0 for i in assignment_list])
  return overlap_assignment

print(aoc_day4_partA('day4-input.txt'))

def aoc_day4_partB(x):
  assignment_list = DataRead(x)[:-1].split('\n')
  overlap_assignment = sum([1 if OverlapTestRefined(i)  else 0 for i in assignment_list])
  return overlap_assignment

print(aoc_day4_partB('day4-input.txt'))
