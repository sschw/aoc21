
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input = [line for line in input.splitlines()]
size = len(input)

shots = [int(val) for val in input[0].split(",")]

boards = []
marked = []
boardAlreadyWon = []

boardId = 0
boardRow = 0
for i in input[1:]:
  if len(i) > 0:
    if len(boards) == boardId:
      boards.append([])
      marked.append([])
      boardAlreadyWon.append(False)
    boards[boardId].append([int(val) for val in i.split()])
    marked[boardId].append([False, False, False, False, False])

    boardRow += 1
    if boardRow == 5:
      boardId += 1
      boardRow = 0

def hasWin(boards, marks, boardId, nextNum):
  added = False
  for i in range(0,5):
    for j in range(0,5):
      if boards[boardId][i][j] == nextNum:
        marks[boardId][i][j] = True
        added = True

  if added:
    win = False
    for i in range(0,5):
      # check whole row true
      # check whole col true
      rowTrue = True
      colTrue = True
      for j in range(0,5):
        rowTrue = rowTrue and marks[boardId][i][j]
        colTrue = colTrue and marks[boardId][j][i]
      win = rowTrue or colTrue
      if win:
        break
    if win:
      sum = 0
      for i in range(0,5):
        for j in range(0,5):
          if marks[boardId][i][j] == False:
            sum += boards[boardId][i][j]
      return sum*nextNum
  return 0

def isLastBoardToWin(boardAlreadyWon):
  numFalse = 0
  for i in boardAlreadyWon:
    if i == False:
      numFalse += 1
  return numFalse == 1

hasNoWin = True
first = True
numId = 0
while hasNoWin:
  num = shots[numId]
  for boardId in range(0, len(boards)):
    if not boardAlreadyWon[boardId]:
      val = hasWin(boards, marked, boardId, num)
      if val != 0:
        if first:
          print("Part One: " + str(val))
          first = False
        if isLastBoardToWin(boardAlreadyWon):
          print("Part Two: " + str(val))
          hasNoWin = False
        boardAlreadyWon[boardId] = True
  numId += 1