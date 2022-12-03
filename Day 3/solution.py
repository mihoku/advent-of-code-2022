def DataRead(a):
  with open(a) as x:
    contents = x.read()
    return contents

def FindOrder(b):
  if(b.isupper()):
    number = ord(b)-38
  else:
    number = ord(b)-96
  return number

def PriorityContent(c):
  compartment_length = int(len(c)/2)
  compartment_a = c[0:compartment_length]
  compartment_b = c[compartment_length:]
  text = ''
  for abc in compartment_a:
    if abc in compartment_b:
      text = abc
  return text

def PriorityGroup(d,e,f):
  text = ''
  for abc in d:
    if abc in e and abc in f:
      text = abc
  return text

def aoc_day3_partA(x):
  containers = DataRead(x)[:-2].split('\n')
  score = sum([FindOrder(PriorityContent(i)) for i in containers])
  return score

print(aoc_day3_partA('day3-input.txt'))

def aoc_day3_partB(x):
  containers = DataRead(x)[:-2].split('\n')
  score = sum([FindOrder(PriorityGroup(containers[i],containers[i+1],containers[i+2])) for i in range(0,len(containers),3)])    
  return score

print(aoc_day3_partB('day3-input.txt'))
