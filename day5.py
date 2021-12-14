
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
    
input = [line for line in input.splitlines()]
size = len(input)

startEnd = [line.split(" -> ") for line in input]

board = []

for x in range(0,1000):
  board.append([])
  for y in range(0,1000):
    board[len(board)-1].append(0)

for i in input:
  i = i.split(" -> ")
  if len(i) > 0:
    start = i[0].split(",")
    end = i[1].split(",")

    startX = int(start[0])
    startY = int(start[1])
    endX = int(end[0])
    endY = int(end[1])
    
    if startX == endX:
      # vertical line
      for i in range(min(startY, endY), max(startY, endY)+1):
        board[i][startX] += 1
    elif startY == endY:
      # horizontal
      for i in range(min(startX, endX), max(startX, endX)+1):
        board[startY][i] += 1
    elif abs(startX-endX) == abs(startY-endY): # diagonal - Part 2
      for i in range(0, abs(startX-endX)+1):
        signX = 1
        if startX > endX:
          signX = -1
        signY = 1
        if startY > endY:
          signY = -1
        board[startY+(i*signY)][startX+(i*signX)] += 1


overlap = 0
for y in range(0,1000):
  print(board[y])
  for x in range(0,1000):
    if board[y][x] > 1:
      overlap += 1


print("Part Two: " + str(overlap))