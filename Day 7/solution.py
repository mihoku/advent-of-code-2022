def DataRead(a):
  with open(a) as x:
    contents = x.read()
    return contents

def TextParser(b):
  contents = b.split('\n')
  contents_dict={'/':0}
  command= ''
  active_directory='/'
  for i in range(1,len(contents)):
    if '$ cd ..' in contents[i]:
      command=''
      ad_member= active_directory.split('-')
      active_directory=active_directory[:-len(ad_member[len(ad_member)-1])-1]
    elif '$ cd ' in contents[i]:
      command=''
      active_directory=active_directory+'-'+contents[i].split(' ')[2]
    elif '$ ls' in contents[i]:
      command='list'
    elif command=='list':
      if contents[i][:4]=='dir ':
        contents_dict[active_directory+'-'+contents[i][4:]]=0
      else:
        current_active_directory = active_directory
        for j in range(0,len(current_active_directory.split('-'))):
          current_ad_member = current_active_directory.split('-')
          contents_dict[current_active_directory] = contents_dict[current_active_directory]+int(contents[i].split(' ')[0])
          current_active_directory=current_active_directory[:-len(current_ad_member[len(current_ad_member)-1])-1]
  return contents_dict

def aoc_day7_partA(input):
  contents = DataRead(input)[:-1]
  disk_content = TextParser(contents)
  disk_content_filtered=dict()
  for (key,value) in disk_content.items():
    if(value<=100000):
      disk_content_filtered[key]=value
  return sum(disk_content_filtered.values())

print(aoc_day7_partA('day7-input.txt'))

def aoc_day7_partB(input):
  contents = DataRead(input)[:-1]
  disk_content = TextParser(contents)
  disk_space = 70000000
  required_space = 30000000
  unused_space = disk_space-disk_content['/']
  space_deficit = required_space-unused_space
  disk_content_filtered=dict()
  for (key,value) in disk_content.items():
    if(value>=space_deficit):
      disk_content_filtered[key]=value
  freeup_directory = sorted(disk_content_filtered.items(), key=lambda x: x[1])[0][1]
  return freeup_directory

print(aoc_day7_partB('day7-input.txt'))
