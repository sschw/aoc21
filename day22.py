with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()


input = input.replace("on x=", "(True,(").replace("off x=", "(False,(").replace("..", ",").replace(",y=", "),(").replace(",z=", "),(")

input_per_line = [eval(line+"))") for line in input.splitlines()]

cube = {}
for line in input_per_line:
  if line[1][1] >= -50 and line[1][0] <= 50 and line[2][1] >= -50 and line[2][0] <= 50 and line[3][1] >= -50 and line[3][0] <= 50:
    for x in range(line[1][0], line[1][1]+1):
      for y in range(line[2][0], line[2][1]+1):
        for z in range(line[3][0], line[3][1]+1):
          cube[(x,y,z)] = line[0]

sum = 0
for i, j in cube.items():
  if j:
    sum += 1
print(sum)

def getOverlapCuboid(cuboid1, cuboid2):
  overlapXStart = max(cuboid1[1][0], cuboid2[1][0])
  overlapXEnd = min(cuboid1[1][1], cuboid2[1][1])
  overlapYStart = max(cuboid1[2][0], cuboid2[2][0])
  overlapYEnd = min(cuboid1[2][1], cuboid2[2][1])
  overlapZStart = max(cuboid1[3][0], cuboid2[3][0])
  overlapZEnd = min(cuboid1[3][1], cuboid2[3][1])
  
  overlapsX = overlapXEnd+1-overlapXStart
  overlapsY = overlapYEnd+1-overlapYStart
  overlapsZ = overlapZEnd+1-overlapZStart
  if overlapsX <= 0 or overlapsY <= 0 or overlapsZ <= 0:
    return 0
  return (None, (overlapXStart, overlapXEnd), (overlapYStart, overlapYEnd), (overlapZStart, overlapZEnd))

def sumCuboids(cuboids):
  removeCuboids = []
  addCuboids = []
  for i in range(0, len(cuboids)):
    cub = cuboids[i]
    if cub[0]:
      addCuboids.append(cub)
    for j in range(0, i):
      pcub = cuboids[j]
      if pcub[0]:
        removeCuboids.append(getOverlapCuboid(cub, pcub))
      else:
        addCuboids.append(getOverlapCuboid(cub, pcub))

  sum = 0
  for c in addCuboids:
    sum += (c[1][1]-c[1][0]+1) * (c[2][1]-c[2][0]+1) * (c[3][1]+1-c[3][0])
  for c in removeCuboids:
    sum -= (c[1][1]+1-c[1][0]) * (c[2][1]+1-c[2][0]) * (c[3][1]+1-c[3][0])
  return sum

print(sumCuboids(input_per_line))


'''sumOn = 0
for lineIdx in range(0, len(input_per_line)):
  line = input_per_line[lineIdx]
  

  for lineAlreadyHandled in input_per_line[0:lineIdx]:
    overlappingRegion = max(min(lineAlreadyHandled[1][1],line[1][1])-max(lineAlreadyHandled[1][0],line[1][0]),0) * max(min(lineAlreadyHandled[2][1],line[2][1])-max(lineAlreadyHandled[2][0],line[2][0]),0) * max(min(lineAlreadyHandled[3][1],line[3][1])-max(lineAlreadyHandled[3][0],line[3][0]),0)

'''