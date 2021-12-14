with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input = [line for line in input.splitlines()]

target = input[0]
rules = {}

input = input[1:]

for inp in input:
  sinp = inp.split(" -> ")
  if len(sinp) > 1:
    rules[sinp[0]] = sinp[1]

for i in range(0, 10):
  tnew = ""
  for l in range(0, len(target)-1):
    ts = target[l:l+2]
    tnew += ts[0] + rules[ts]
  tnew += ts[1]
  target = tnew

counts = {}
for c in list(target):
  if c in counts:
    counts[c] += 1
  else:
    counts[c] = 1
vals = list(counts.values())
vals.sort()
print("Part One: " + str(vals[-1]-vals[0]))

for i in range(0, 30):
  print(i+10)
  tnew = ""
  for l in range(0, len(target)-1):
    ts = target[l:l+2]
    tnew += ts[0] + rules[ts]
  tnew += ts[1]
  target = tnew

counts = {}
for c in list(target):
  if c in counts:
    counts[c] += 1
  else:
    counts[c] = 1
vals = list(counts.values())
vals.sort()
print("Part Two: " + str(vals[-1]-vals[0]))

# too slow. see cpp implementation.