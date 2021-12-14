with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
  input = input_file.read()

input_per_line = [list(line) for line in input.splitlines()]
size = len(input_per_line)

validLines = []
corruptedLines = []
invScore = 0
valScores = []

def getScore(c):
  if c == ")":
    return 3
  if c == "]":
    return 57
  if c == "}":
    return 1197
  if c == ">":
    return 25137

def closes(c, cToMatch):
  if c == ")":
    return cToMatch == "("
  if c == "]":
    return cToMatch == "["
  if c == "}":
    return cToMatch == "{"
  if c == ">":
    return cToMatch == "<"
  
def calcValidScore(l):
  s = 0
  while(len(l) > 0):
    last = l.pop()
    s *= 5
    if last == "(":
      s += 1
    if last == "[":
      s += 2
    if last == "{":
      s += 3
    if last == "<":
      s += 4
  return s

for line in input_per_line:
  idToLookAt = []
  valid = True
  id = -1
  for c in line:
    id += 1
    if c == "{" or c == "[" or c == "("  or c == "<":
      idToLookAt.append(c)
    elif c == "}" or c == "]" or c == ")"  or c == ">":
      if len(idToLookAt) > 0:
        cToMatch = idToLookAt.pop()
        if closes(c, cToMatch):
          pass
        else:
          valid = False
          invScore += getScore(c)
          break
      else: 
        valid = False
        invScore += getScore(c)
        break
  if valid:
    valScores.append(calcValidScore(idToLookAt))
    validLines.append(line)
  else:
    corruptedLines.append(line)

print("Part One: " + str(invScore))
valScores.sort()
print("Part Two: " + str(valScores[int(len(valScores)/2)]))