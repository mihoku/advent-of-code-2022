def DataRead(a):
  with open(a) as x:
    contents = x.read()
    return contents

def ExcerptTester(b):
  return sum([1 if b.count(b[i])>1 else 0 for i in range(0,len(b))])==0

def aoc_day6_partA(text):
  content = DataRead(text)
  packet_marker = 3
  for i in range(0,len(content)):
    packet_marker+=1    
    if ExcerptTester(content[i:i+4]):
      break
  return packet_marker

print(aoc_day6_partA('day6-input.txt'))

def aoc_day6_partB(text):
  content = DataRead(text)
  message_marker = 13
  for i in range(0,len(content)):
    message_marker+=1    
    if ExcerptTester(content[i:i+14]):
      break
  return message_marker

print(aoc_day6_partB('day6-input.txt'))
