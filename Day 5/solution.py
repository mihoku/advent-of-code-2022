def DataRead(a):
  with open(a) as x:
    contents = x.read()
    return contents

def LimitFinder(text):
  limiter = text[text.find('\n 1'):text.find('\n\n')+2]
  return limiter

def StacksReader(b):
  raw_stacks = b[:b.find(LimitFinder(b))]
  raw_stacks = raw_stacks.replace('     ',' [ ] ').replace('   \n','[ ]\n')
  raw_stacks = raw_stacks.replace('     ',' [ ] ').replace('    ','[ ] ')
  raw_stacks = raw_stacks.replace('] [','|').replace('[','').replace(']','')
  original_stack = dict([(str(i),[]) for i in range(1,10)])
  for row in raw_stacks.split('\n'):
    columns = [col for col in row.split('|')]
    for i in range(0,9):
      if columns[i]!=' ':
        original_stack[str(i+1)].append((columns[i]))
  return original_stack

def ArrangementReader(c):
  arrangement = c[c.find(LimitFinder(c))+len(LimitFinder(c)):]
  arrangement = arrangement.replace('move ','').replace(' from ','|').replace(' to ','|')
  return arrangement

def CrateMover9000(d,e):
  command = d.split('|')
  for i in range(0,int(command[0])):
    e[command[2]] = [e[command[1]].pop(0)]+e[command[2]]
  return e

def CrateMover9001(d,e):
  moved=[]
  command = d.split('|')
  for i in range(0,int(command[0])):
    moved.append(e[command[1]].pop(0))
  e[command[2]] = moved+e[command[2]]
  return e

def StackAnalyzer(f):
  keyword = ''
  for i in range(1,10):
    keyword+=f[str(i)][0]
  return keyword

def aoc_day5_partA(input):
  stacks = StacksReader(DataRead('day5-input.txt'))
  arrangement = ArrangementReader(DataRead('day5-input.txt'))
  for i in arrangement[:-1].split('\n'):
    stacks = CrateMover9000(i,stacks)
  keyword = StackAnalyzer(stacks)
  return keyword

print(aoc_day5_partA('day5-input.txt'))

def aoc_day5_partB(input):
  stacks = StacksReader(DataRead('day5-input.txt'))
  arrangement = ArrangementReader(DataRead('day5-input.txt'))
  for i in arrangement[:-1].split('\n'):
    stacks = CrateMover9001(i,stacks)
  keyword = StackAnalyzer(stacks)
  return keyword

print(aoc_day5_partB('day5-input.txt'))
