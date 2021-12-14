with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

input = [line.split(",") for line in input.splitlines()]
coordinates = []
folds = []

# max values in this dir
maxVal = {"x": 0, "y": 0}

for i in input:
  if len(i) == 2:
    coordinates.append({"x": int(i[0]), "y": int(i[1])})
    if coordinates[-1]["x"] > maxVal["x"]:
      maxVal["x"] = coordinates[-1]["x"]
    if coordinates[-1]["y"] > maxVal["y"]:
      maxVal["y"] = coordinates[-1]["y"]
  elif len(i) == 1 and len(i[0]) > 0:
    s = i[0].split("=")
    if len(s) > 1:
      direction = list(s[0])[-1]
      fold = int(s[1])
      folds.append({"dir": direction, "fold": fold})


def doFold(fold, coordinates):
  for i in range(0, len(coordinates)):
    if coordinates[i][fold["dir"]] > fold["fold"]:
      coordinates[i][fold["dir"]] = coordinates[i][fold["dir"]] - (coordinates[i][fold["dir"]]-fold["fold"])*2
      maxVal[fold["dir"]] = fold["fold"]

doFold(folds[0], coordinates)

coordSet = set()
for i in coordinates:
  coordSet.add(i["x"]*100000+i["y"])
print("Part One: " + str(len(coordSet)))

for i in folds[1:]:
  doFold(i, coordinates)

mapToDisp = []
for y in range(0, maxVal["y"]):
  mapToDisp.append([" "]*maxVal["x"])
  
for i in coordinates:
  mapToDisp[i["y"]][i["x"]] = "#"

print("Part Two: ")
for y in mapToDisp:
  print("".join(y))
