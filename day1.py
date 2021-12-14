
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input_as_int = [int(line) for line in input.splitlines()]
size = len(input_as_int)
found = False
first = True
inc = 0
prevVal = 0

for val in input_as_int:
    if not first:
      if prevVal < val:
        inc += 1
    first = False
    prevVal = val

print("Part One:" + str(inc))
prevVal = 0
prevPrevVal = 0
prevPrevPrevVal = 0
valIdx = 0
valNumber = 0
inc = 0
first = 0
for val in input_as_int:
  if first >= 3:
    if val > prevPrevPrevVal:
      inc += 1
  prevPrevPrevVal = prevPrevVal
  prevPrevVal = prevVal
  prevVal = val
  first += 1

print("Part Two:" + str(inc))
