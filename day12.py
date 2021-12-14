with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input = [line.split("-") for line in input.splitlines()]

nodeList = {}

for line in input:
  if line[0] in nodeList:
    nodeList[line[0]].append(line[1])
  else:
    nodeList[line[0]] = [line[1]]
  
  if line[1] in nodeList:
    nodeList[line[1]].append(line[0])
  else:
    nodeList[line[1]] = [line[0]]

def findAllPaths(cur, blocked):
  if cur == "end":
    return 1
  if cur.islower():
    blocked.append(cur)
  s = 0
  for i in nodeList[cur]:
    if not i in blocked:
      s += findAllPaths(i, blocked)
  if cur.islower():
    blocked.remove(cur)
  return s

print("Part One: " + findAllPaths("start", []))

def findAllPaths2(cur, allowOnce, blocked):
  if cur == "end":
    return 1
  if cur.islower():
    blocked.append(cur)
  s = 0
  for i in nodeList[cur]:
    if i == "start":
      continue
    notInBlocked = not i in blocked
    if notInBlocked or allowOnce:
      s += findAllPaths2(i, notInBlocked and allowOnce, blocked)
  if cur.islower():
    blocked.remove(cur)
  return s

print("Part Two: " + findAllPaths2("start", True, []))