with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input = [line for line in input.splitlines()]
size = len(input)

oneBits = []

for i in range(0, len(input[0])):
  oneBits.append(0)

for row in input:
  bitNumber = len(row)-1
  for bit in list(row):
    if bit == "1":
      oneBits[bitNumber] += 1
    bitNumber -= 1

bitNumber = 0
gamma = 0
epsilon = 0
for i in oneBits:
  if i > size/2:
    gamma += pow(2, bitNumber)
  if i < size/2:
    epsilon += pow(2, bitNumber)
  bitNumber += 1

print("Part One:" + str(gamma*epsilon))


def oneBitsMinusHalf(l, idx):
  v = 0
  m = len(l)
  for i in list(l):
    if i[idx] == "1":
      v += 1
  return v - m/2

idx = 0
pos = 0
oxygen = input.copy()
vals = []
vals.append(oneBitsMinusHalf(oxygen, 0))
while len(oxygen) > 1:
  bits = list(oxygen[pos])
  bit = bits[idx]
  oneBitsSize = vals[idx]
  if oneBitsSize >= 0 and bit == "0":
    # consider one
    oxygen.remove(oxygen[pos])
    pos -= 1
  elif oneBitsSize < 0 and bit == "1":
    # consider zero
    oxygen.remove(oxygen[pos])
    pos -= 1
  pos += 1
  if pos == len(oxygen) and len(oxygen) > 1:
    pos = 0
    idx += 1
    vals.append(oneBitsMinusHalf(oxygen, idx))


idx = 0
pos = 0
co2scrubber = input.copy()
vals = []
vals.append(oneBitsMinusHalf(co2scrubber, 0))
while len(co2scrubber) > 1:
  bits = list(co2scrubber[pos])
  bit = bits[idx]
  oneBitsSize = vals[idx]
  if oneBitsSize < 0 and bit == "0":
    # consider one
    co2scrubber.remove(co2scrubber[pos])
    pos -= 1
  elif oneBitsSize >= 0 and bit == "1":
    # consider zero
    co2scrubber.remove(co2scrubber[pos])
    pos -= 1
  pos += 1
  if pos == len(co2scrubber) and len(co2scrubber) > 1:
    pos = 0
    idx += 1
    vals.append(oneBitsMinusHalf(co2scrubber, idx))

bitNumber = len(oneBits)-1
co2Val = 0
oxyVal = 0
for i in range(0,len(oneBits)):
  co2Val += int(co2scrubber[0][i])*pow(2, bitNumber)
  oxyVal += int(oxygen[0][i])*pow(2, bitNumber)
  bitNumber -= 1

print("Part Two: " + str(oxyVal*co2Val))