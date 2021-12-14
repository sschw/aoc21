with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input = [list(line) for line in input.splitlines()]
for y in range(0, len(input)):
  for x in range(0, len(input[y])):
    input[y][x] = int(input[y][x])

def isLowPoint(map, x, y):
  val = map[y][x]
  maxX = len(map[0])-1
  maxY = len(map)-1
  
  for i in range(-1, 2):
    if min(maxY, max(y+i, 0)) != y and map[min(maxY, max(y+i, 0))][x] <= val:
      return False
    if min(maxX, max(x+i, 0)) != x and map[y][min(maxX, max(x+i, 0))] <= val:
      return False
  return True

sum = 0
for y in range(0, len(input)):
  for x in range(0, len(input[y])):
    if isLowPoint(input, x, y):
      sum += input[y][x]+1

print("Part One: " + str(sum))

def setBasin(map, x, y, id):
  val = map[y][x]
  if val == 9 or val < 0:
    return
  map[y][x] = id

  maxX = len(map[0])-1
  maxY = len(map)-1
  
  for i in range(-1, 2):
    if min(maxY, max(y+i, 0)) != y and map[min(maxY, max(y+i, 0))][x] >= 0:
      setBasin(map, x, min(maxY, max(y+i, 0)), id)
    if min(maxX, max(x+i, 0)) != x and map[y][min(maxX, max(x+i, 0))] >= 0:
      setBasin(map, min(maxX, max(x+i, 0)), y, id)

id = -1
for y in range(0, len(input)):
  for x in range(0, len(input[y])):
    val = input[y][x]
    if val < 9 and val >= 0:
      setBasin(input, x, y, id)
      id -= 1

def basinSizes(map, minId):
  basinSizes = []
  for i in range(-1, minId, -1):
    basinSizes.append(0)
    for y in range(0, len(map)):
      for x in range(0, len(map[y])):
        if map[y][x] == i:
          basinSizes[-(i+1)] += 1
  return basinSizes

vals = basinSizes(input, id)
vals.sort()
print("Part Two: " + str(vals[len(vals)-1]*vals[len(vals)-2]*vals[len(vals)-3]))