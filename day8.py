numToPosVal = [[], [], [1], [7], [4], [2, 3, 5], [0, 6, 9], [8]]

# a = 0, b = 1, c = 2, d = 3, e = 4, f = 5, g = 6
posPos = [[0, 1, 2, 4, 5, 6], [2, 5], [0, 2, 3, 4, 6], [0, 2, 3, 5, 6], [1, 2, 3, 5], [0, 1, 3, 5, 6], [0, 1, 3, 4, 5, 6], [0, 2, 5], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 5, 6]]

# can be every segment at every segment pos
new7Segment = [['a', 'b', 'c', 'd', 'e', 'f', 'g'], ['a', 'b', 'c', 'd', 'e', 'f', 'g'], ['a', 'b', 'c', 'd', 'e', 'f', 'g'], ['a', 'b', 'c', 'd', 'e', 'f', 'g'], ['a', 'b', 'c', 'd', 'e', 'f', 'g'], ['a', 'b', 'c', 'd', 'e', 'f', 'g'], ['a', 'b', 'c', 'd', 'e', 'f', 'g']]


with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
  input = input_file.read()

input_per_line = [line for line in input.splitlines()]
size = len(input_per_line)

inputOutputPerLine = [line.split(" | ") for line in input_per_line]

su = 0 
for iO in inputOutputPerLine:
  out = iO[1]
  vals = out.split(" ")
  for i in vals:
    if len(i) == 2 or len(i) == 4 or len(i) == 3 or len(i) == 7:
      su += 1

# 7 1 = a -> n, [c,f] -> [m,o] 7 1 4 

print("Part One: " + str(su))

def filterSeg(patterns):
  segDef = new7Segment.copy()
  # find 1
  for pattern in patterns:
    if len(pattern) == 2:
      segDef[2] = []
      segDef[5] = []
      for p in list(pattern):
        segDef[2].append(p)
        segDef[5].append(p)
      break
  # find 7  
  for pattern in patterns:
    if len(pattern) == 3:
      segDef[0] = []
      for p in list(pattern):
        num = p
        if not num in segDef[2]:
          segDef[0].append(num)
      break
  # find 4
  for pattern in patterns:
    if len(pattern) == 4:
      segDef[1] = []
      segDef[3] = []
      for p in list(pattern):
        num = p
        if not num in segDef[2]:
          segDef[1].append(num)
          segDef[3].append(num)
      break
  # find 6,9,0
  patterns069 = []
  for pattern in patterns:
    if len(pattern) == 6:
      patterns069.append([p for p in list(pattern)])
  
  pIntersect = [set(patterns069[0]).intersection(patterns069[1]).intersection(patterns069[2]).difference(segDef[0]).difference(segDef[1]).difference(segDef[2])]
  segDef[6] = list(pIntersect[0])
  pIntersect = [set(patterns069[0]).intersection(patterns069[1]).intersection(patterns069[2]).difference(segDef[0]).intersection(segDef[1]).difference(segDef[2])]
  segDef[1] = list(pIntersect[0])
  pIntersect = [set(patterns069[0]).intersection(patterns069[1]).intersection(patterns069[2]).difference(segDef[0]).difference(segDef[3]).difference(segDef[6])]
  segDef[5] = list(pIntersect[0])
  segDef[2] = list(set(segDef[2]).difference(segDef[5]))
  segDef[3] = list(set(segDef[3]).difference(segDef[1]))
  segDef[4] = list(set(segDef[4]).difference(segDef[0]).difference(segDef[1]).difference(segDef[2]).difference(segDef[3]).difference(segDef[5]).difference(segDef[6]))
  return segDef

def numList(segDef):
  numList = []

  for i in range(0, 10):
    cur = ""
    for j in posPos[i]:
      cur += segDef[j][0]
    numList.append(cur)
  return numList

def findNum(numList, pattern):
  for i in range(0, 10):
    if set(numList[i]) == set(pattern):
      return i
  return -1

s = 0
for iO in inputOutputPerLine:
  inp = iO[0]
  out = iO[1]
  curSeg = filterSeg(inp.split(" "))
  l = numList(curSeg)
  mul = 1000
  num = 0
  for o in out.split(" "):
    num += findNum(l, o)*mul
    mul /= 10
  s += num
print("Part Two: " + str(s))