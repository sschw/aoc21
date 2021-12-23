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

def combine(cuboid1, cuboid2):
  cuboids = [cuboid1] # keep first one
  overlapXStart = max(cuboid1[1][0], cuboid2[1][0])
  overlapXEnd = min(cuboid1[1][1], cuboid2[1][1])
  overlapYStart = max(cuboid1[2][0], cuboid2[2][0])
  overlapYEnd = min(cuboid1[2][1], cuboid2[2][1])
  overlapZStart = max(cuboid1[3][0], cuboid2[3][0])
  overlapZEnd = min(cuboid1[3][1], cuboid2[3][1])
  xPos = [cuboid2[1][0], overlapXStart, overlapXEnd, cuboid2[1][1]]
  yPos = [cuboid2[2][0], overlapYStart, overlapYEnd, cuboid2[2][1]]
  zPos = [cuboid2[3][0], overlapZStart, overlapZEnd, cuboid2[3][1]]
  for x in range(0, len(xPos)-1):
    for y in range(0, len(yPos)-1):
      for z in range(0, len(zPos)-1):
        if xPos == 1 and yPos == 1 and zPos == 1:
          # overlapping rectangle, we already have this.
          pass
        elif xPos[x] >= xPos[x+1] or yPos[y] >= yPos[y+1] or zPos[z] >= zPos[z+1]:
          # no overlapping.
          pass
        else:
          cuboids.append((cuboid2[0], (xPos[x], xPos[x+1]), (yPos[x], yPos[x+1]), (zPos[x], zPos[x+1])))
  return cuboids

def remove(cuboid1, cuboid2):
  cuboids = []
  overlapXStart = max(cuboid1[1][0], cuboid2[1][0])
  overlapXEnd = min(cuboid1[1][1], cuboid2[1][1])
  overlapYStart = max(cuboid1[2][0], cuboid2[2][0])
  overlapYEnd = min(cuboid1[2][1], cuboid2[2][1])
  overlapZStart = max(cuboid1[3][0], cuboid2[3][0])
  overlapZEnd = min(cuboid1[3][1], cuboid2[3][1])
  xPos = [cuboid1[1][0], overlapXStart, overlapXEnd, cuboid1[1][1]]
  yPos = [cuboid1[2][0], overlapYStart, overlapYEnd, cuboid1[2][1]]
  zPos = [cuboid1[3][0], overlapZStart, overlapZEnd, cuboid1[3][1]]
  for x in range(0, len(xPos)-1):
    for y in range(0, len(yPos)-1):
      for z in range(0, len(zPos)-1):
        if xPos == 1 and yPos == 1 and zPos == 1:
          # overlapping rectangle, we don't want this one anymore.
          pass
        elif xPos[x] >= xPos[x+1] or yPos[y] >= yPos[y+1] or zPos[z] >= zPos[z+1]:
          # no overlapping.
          pass
        else:
          cuboids.append((cuboid2[0], (xPos[x], xPos[x+1]), (yPos[x], yPos[x+1]), (zPos[x], zPos[x+1])))

def sumCuboids(cuboids):
  sum = 0
  for i in cuboids:
    sum += (i[0][1] - i[0][0]) * (i[1][1] - i[1][0]) * (i[2][1] - i[2][0])
  return sum

cuboids = [input_per_line[0]]
for c in input_per_line[1:]:
  if c[0] == False:
    newCuboids = []
    for c2 in cuboids:


'''sumOn = 0
for lineIdx in range(0, len(input_per_line)):
  line = input_per_line[lineIdx]
  

  for lineAlreadyHandled in input_per_line[0:lineIdx]:
    overlappingRegion = max(min(lineAlreadyHandled[1][1],line[1][1])-max(lineAlreadyHandled[1][0],line[1][0]),0) * max(min(lineAlreadyHandled[2][1],line[2][1])-max(lineAlreadyHandled[2][0],line[2][0]),0) * max(min(lineAlreadyHandled[3][1],line[3][1])-max(lineAlreadyHandled[3][0],line[3][0]),0)

'''