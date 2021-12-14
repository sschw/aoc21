
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input = [line for line in input.splitlines()]
size = len(input)

lanternfishs = [int(val) for val in input[0].split(",")]

counters = [0, 0, 0, 0, 0, 0, 0]
afterindexonce = [0, 0, 0, 0, 0, 0, 0]

for i in lanternfishs:
  counters[i] += 1


for i in range(0, 80):
  if counters[i%7] > 0:
    afterindexonce[(i+2)%7] += counters[i%7]
  if afterindexonce[i%7] != 0:
    counters[i%7] += afterindexonce[i%7]
    afterindexonce[i%7] = 0

sumL = 0
for i in counters:
  sumL += i

for i in afterindexonce:
  sumL += i

print("Part One: " + str(sumL))

counters = [0, 0, 0, 0, 0, 0, 0]
afterindexonce = [0, 0, 0, 0, 0, 0, 0]

for i in lanternfishs:
  counters[i] += 1


for i in range(0, 256):
  if counters[i%7] > 0:
    afterindexonce[(i+2)%7] += counters[i%7]
  if afterindexonce[i%7] != 0:
    counters[i%7] += afterindexonce[i%7]
    afterindexonce[i%7] = 0

sumL = 0
for i in counters:
  sumL += i

for i in afterindexonce:
  sumL += i

print("Part Two: " + str(sumL))