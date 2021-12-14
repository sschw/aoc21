
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input = [line for line in input.splitlines()]
size = len(input)

crabs = [int(val) for val in input[0].split(",")]

fuel = []
miC = min(crabs)
maC = max(crabs)
for i in range(miC, maC+1):
  fuel.append(0)
for crab in crabs:
  for i in range(miC, maC+1):
    id = i-miC
    fuel[id] += abs(crab-i)
print("Part One: " + str(min(fuel)))


fuel = []
miC = min(crabs)
maC = max(crabs)
for i in range(miC, maC+1):
  fuel.append(0)
for crab in crabs:
  for i in range(miC, maC+1):
    id = i-miC
    n = abs(crab-i)
    fuel[id] += n*(n+1)/2
print("Part Two: " + str(min(fuel)))