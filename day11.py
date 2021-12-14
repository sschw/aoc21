with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input = [list(line) for line in input.splitlines()]
blocked = []
for y in range(0, len(input)):
  blocked.append([])
  for x in range(0, len(input[y])):
    input[y][x] = int(input[y][x])
    blocked[y].append(False)




def flash(map, blocked, x, y):
  if blocked[y][x]:
    return 0
  map[y][x] = (map[y][x] + 1)%10

  if map[y][x] != 0:
    return 0
  
  blocked[y][x] = True
  s = 1
  for yi in range(max(0, y-1), min(len(input), y+2)):
    for xi in range(max(0, x-1), min(len(input), x+2)):
      if xi != x or yi != y:
        s += flash(map, blocked, xi, yi)
  return s


flashes = 0
for i in range(0, 100):
  for y in range(0, len(input)):
    for x in range(0, len(input)):
      blocked[y][x] = False
  for y in range(0, len(input)):
    for x in range(0, len(input)):
      flashes += flash(input, blocked, y, x)

  
  #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
  #      for row in input]))
  #print()

print("Part One: " + str(flashes))

it = 100
while(sum(sum(input, [])) > 0):
  for y in range(0, len(input)):
    for x in range(0, len(input)):
      blocked[y][x] = False
  for y in range(0, len(input)):
    for x in range(0, len(input)):
      flash(input, blocked, y, x)
  #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
  #      for row in input]))
  #print()

  it += 1

print("Part Two: " + str(it))