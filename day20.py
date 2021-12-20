with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()


input = input.replace(".", "0").replace("#", "1")

input = [line for line in input.splitlines()]

alg = [int(i) for i in list(input[0])]

input = [list(line) for line in input[1:] if len(line) > 0]
inp = [[int(i) for i in row] for row in input]

def getValue(inp, centerX, centerY):
  sum = 0
  for y in range(-1, 2):
    for x in range(-1, 2):
      # if out of range, use pos (0,0) which should always be the halo.
      posX = x+centerX
      posY = y+centerY
      if x+centerX < 0 or x+centerX >= len(inp[0]):
        posX = 0
      if y+centerY < 0 or y+centerY >= len(inp):
        posY = 0
      sum += pow(2, 8-(3*(y+1))-(x+1))*inp[posY][posX]
  return sum

def changeImg(inp, out, alg):
  for y in range(0, len(inp)):
    for x in range(0, len(inp[0])):
      out[y][x] = alg[getValue(inp, x, y)]

def printArr(arr):
  for row in arr:
    for val in row:
      if val == 1:
        print("#", end="")
      else:
        print(" ", end="")
    print()

for i in range(0, 25):
  for row in inp:
    row.insert(0, 0)
    row.insert(0, 0)
    row.append(0)
    row.append(0)
  inp.insert(0, [0 for i in inp[0]])
  inp.insert(0, [0 for i in inp[0]])
  inp.append([0 for i in inp[0]])
  inp.append([0 for i in inp[0]])
  out = [[int(0) for i in row] for row in inp]

  changeImg(inp, out, alg)
  changeImg(out, inp, alg)
  

print(sum(sum(inp, [])))