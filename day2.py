
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input_per_line = [line for line in input.splitlines()]
size = len(input_per_line)
h = 0
d = 0
p1 = 0
p2 = 0

for val in input_per_line:
  vS = val.split(" ")
  if vS[0] == "forward":
    h += int(vS[1])
  if vS[0] == "down":
    d += int(vS[1])
  if vS[0] == "up":
    d -= int(vS[1])

p1 = h*d
print("Part One:" + str(p1))

h = 0
d = 0
aim = 0

for val in input_per_line:
  vS = val.split(" ")
  if vS[0] == "forward":
    h += int(vS[1])
    d += int(vS[1])*aim
  if vS[0] == "down":
    aim += int(vS[1])
  if vS[0] == "up":
    aim -= int(vS[1])

p2 = h*d
print("Part Two:" + str(p2))
