def DataRead(a):
  with open(a) as x:
    contents = x.read()
    return contents

def VisibleTrees(b):
  forest = b.split('\n')
  visible_trees = 0
  for row_number in range(0,len(forest)):
    if row_number in [0,len(forest)-1]:
      visible_trees+=len(forest[row_number])
    else:
      visible_trees+=2
      for tree_number in range(1,len(forest[row_number])-1):
        left_status = True
        for left_tree_number in range(0,tree_number):
          if int(forest[row_number][tree_number])<=int(forest[row_number][left_tree_number]):
            left_status=False
        right_status = True
        for right_tree_number in range(tree_number+1,len(forest[row_number])):
          if int(forest[row_number][tree_number])<=int(forest[row_number][right_tree_number]):
            right_status=False
        up_status = True
        for up_tree_number in range(0,row_number):
          if int(forest[row_number][tree_number])<=int(forest[up_tree_number][tree_number]):
            up_status=False
        down_status=True
        for down_tree_number in range(row_number+1,len(forest)):
          if int(forest[row_number][tree_number])<=int(forest[down_tree_number][tree_number]):
            down_status=False
        if left_status or right_status or up_status or down_status:
          visible_trees+=1
  return visible_trees

def ScenicView(c):
  forest = c.split('\n')
  scenic_scores = []
  for row_number in range(1,len(forest)-1):
    for tree_number in range(1,len(forest[row_number])-1):
      left_status = tree_number
      for left_tree_number in range(0,tree_number):
        if int(forest[row_number][tree_number])<=int(forest[row_number][left_tree_number]):
          left_status=tree_number-left_tree_number
      right_status = 0
      for right_tree_number in range(tree_number+1,len(forest[row_number])):
        right_status+=1
        if int(forest[row_number][tree_number])<=int(forest[row_number][right_tree_number]):
          break
      up_status = row_number
      for up_tree_number in range(0,row_number):
        if int(forest[row_number][tree_number])<=int(forest[up_tree_number][tree_number]):
          up_status=row_number-up_tree_number
      down_status=0
      for down_tree_number in range(row_number+1,len(forest)):
        down_status+=1
        if int(forest[row_number][tree_number])<=int(forest[down_tree_number][tree_number]):
          break
      scenic_scores.append(up_status*left_status*down_status*right_status)
  return max(scenic_scores)

def aoc_day8_partA(input):
  contents = DataRead(input)[:-1]
  return VisibleTrees(contents)

print(aoc_day8_partA('day8-input.txt'))

def aoc_day8_partB(input):
  contents = DataRead(input)[:-1]
  return ScenicView(contents)

print(aoc_day8_partB('day8-input.txt'))
