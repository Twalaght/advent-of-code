#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

coords = data[:799]

for i in range(len(coords)):
	coords[i] = coords[i].split(",")
	coords[i] = (int(coords[i][0]), int(coords[i][1]))

folds = data[800:]

for i in range(len(folds)):
	folds[i] = folds[i].split()[-1].split("=")
	folds[i][1] = int(folds[i][1])

silver = None

for fold in folds:
	tmp = []

	if fold[0] == "x":
		for i in range(len(coords)):
			pnt = [coords[i][0], coords[i][1]]

			if coords[i][0] > fold[1]:
				pnt[0] = fold[1] + (fold[1] - pnt[0])

			pnt = tuple(pnt)

			if pnt not in tmp:
				tmp.append(pnt)

	else:
		for i in range(len(coords)):
			pnt = [coords[i][0], coords[i][1]]

			if coords[i][1] > fold[1]:
				pnt[1] = fold[1] + (fold[1] - pnt[1])

			pnt = tuple(pnt)

			if pnt not in tmp:
				tmp.append(pnt)

	if silver is None:
		silver = len(tmp)

	coords = tmp

print(f"Silver: {silver}")

output = []
for i in range(7):
	tmp = []
	for j in range(41):
		tmp.append(" ")

	output.append(tmp)

for i in coords:
	output[i[1]][i[0]] = "#"

print("Gold:")

for i in output:
	print("".join(i))
