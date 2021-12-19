import math

# rotations
def applyRotation(value, rotation):
  xSign = math.copysign(1, rotation[0])
  xIdx = int(rotation[0]*xSign)-1
  ySign = math.copysign(1, rotation[1])
  yIdx = int(rotation[1]*ySign)-1
  zSign = math.copysign(1, rotation[2])
  zIdx = int(rotation[2]*zSign)-1

  return (value[xIdx]*xSign, value[yIdx]*ySign, value[zIdx]*zSign)

# We have a table of rotations
# id of value to read and sign of value
rotations = [
  (1, 2, 3),
  (1, -3, 2),
  (1, -2, -3),
  (1, 3, -2),
  (3, 2, -1),
  (2, -3, -1),
  (-3, -2, -1),
  (-2, 3, -1),
  (-1, 2, -3),
  (-1, -3, -2),
  (-1, -2, 3),
  (-1, 3, 2),
  (-3, 2, 1),
  (-2, -3, 1),
  (3, -2, 1),
  (2, 3, 1),
  (-2, 1, 3),
  (3, 1, 2),
  (2, 1, -3),
  (-3, 1, -2),
  (2, -1, 3),
  (-3, -1, 2),
  (-2, -1, -3),
  (3, -1, -2),
]

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input = [line for line in input.splitlines()]

scannerResults = []

for line in input:
  if line.startswith("---"):
    scannerResults.append(set())
  elif line == "":
    pass
  else:
    scannerResults[-1].add(eval("(" + line + ")"))

def subtr(t1, t2):
  if len(t1) == 2:
    return (t1[0]-t2[0], t1[1]-t2[1])
  return (t1[0]-t2[0], t1[1]-t2[1], t1[2]-t2[2])

def findCommonPoints(sc1, sc2):
  # test for all points in first scanner
  for s1 in sc1:
    # rotate second scanner points into all 24 directions
    for rot in rotations:
      # test for all points in second scanner
      for s2 in sc2:
        rotS2 = applyRotation(s2, rot)
        # assume s2-s1 is distance between the two scans.
        dist = subtr(rotS2, s1)

        # transform s2 into s1 using the distance
        s2t = set(subtr(applyRotation(pos, rot), dist) for pos in sc2)

        if len(s2t & sc1) >= 12:
          return s2t, dist, rot
  return None

transformedScannerResults = []
transformedPos = []
transformedRot = []
for s in scannerResults:
  transformedScannerResults.append([])
  transformedPos.append([])
  transformedRot.append([])
transformedScannerResults[0] = scannerResults[0]
transformedPos[0] = (0, 0, 0)
transformedRot[0] = (1, 2, 3)

changed = True
newlyAdded = [scannerResults[0]]
while changed:
  toCheck = newlyAdded
  newlyAdded = []
  scannerId = 0
  changed = False
  for s in scannerResults:
    if transformedScannerResults[scannerId] == []:
      for ts in toCheck:
        if ts != []:
          f = findCommonPoints(ts, s)
          if f != None:
            changed = True
            transformedScannerResults[scannerId] = f[0]
            newlyAdded.append(f[0])
            transformedPos[scannerId] = f[1]
            transformedRot[scannerId] = f[2]
    scannerId += 1

bcns = set()
for ts in transformedScannerResults:
  for r in ts:
    bcns.add(r)

print(len(bcns))

def manhatten(p1, p2):
  sb = subtr(p1, p2)
  return abs(sb[0]) + abs(sb[1]) + abs(sb[2])

maxDist = 0
for p1 in transformedPos:
  for p2 in transformedPos:
    m = manhatten(p1, p2)
    if m > maxDist:
      maxDist = m

print(maxDist)