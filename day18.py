import copy

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input = [eval(line) for line in input.splitlines()]

def addToInnerstLeft(pair, val):
  while isinstance(pair[0], list):
    pair = pair[0]
  pair[0] += val
  
def addToInnerstRight(pair, val):
  while isinstance(pair[1], list):
    pair = pair[1]
  pair[1] += val

def explode(pair, depth=1):
  leftOut = 0
  rightOut = 0
  if isinstance(pair[0], list):
    leftOut, explVal, right = explode(pair[0], depth+1)
    pair[0] = explVal
    if isinstance(pair[1], int):
      pair[1] += right
    else:
      addToInnerstLeft(pair[1], right)
  if isinstance(pair[1], list):
    left, explVal, rightOut = explode(pair[1], depth+1)
    pair[1] = explVal
    if isinstance(pair[0], int):
      pair[0] += left
    else:
      addToInnerstRight(pair[0], left)

  if isinstance(pair[0], int) and isinstance(pair[1], int) and depth >= 5:
    return pair[0], 0, pair[1]
  return leftOut, pair, rightOut

def split(pair):
  if isinstance(pair, list):
    val = split(pair[0])
    if val != None:
      return [val, pair[1]]
    val = split(pair[1])
    if val != None:
      return [pair[0], val]
  else:
    if pair > 9:
      return [int(pair/2), int((pair+1)/2)]
  return None

def reduce(p):
  running = True
  while running:
    pNew = split(explode(p)[1])
    print
    if pNew == None:
      running = False
    else:
      p = pNew
  return p

def calcMagnitude(p):
  sum = 0
  if isinstance(p[0], list):
    sum += 3*calcMagnitude(p[0])
  else:
    sum += 3*p[0]
  if isinstance(p[1], list):
    sum += 2*calcMagnitude(p[1])
  else:
    sum += 2*p[1]
  return sum
  
inputCopy = copy.deepcopy(input)
pair = inputCopy[0]
for l in inputCopy[1:]:
  pair = reduce([pair, l])
print(pair)
print("Magnitude: " + str(calcMagnitude(pair)))

maxMag = 0
for h in input:
  for i in input:
    if h != i:
      mag = calcMagnitude(reduce([copy.deepcopy(h), copy.deepcopy(i)]))
      if mag > maxMag:
        maxMag = mag
      
      mag = calcMagnitude(reduce([copy.deepcopy(i), copy.deepcopy(h)]))
      if mag > maxMag:
        maxMag = mag

print(maxMag)