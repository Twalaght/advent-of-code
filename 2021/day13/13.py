#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

coords = [[int(x) for x in line.split(",")] for line in data[:799]]
folds = [[x for x in line.split()[-1].split("=")] for line in data[800:]]
folds =	[[x[0], int(x[1])] for x in folds]

silver = None
for fold in folds:
	tmp = []
	axis = 0 if fold[0] == "x" else 1

	for coord in coords:
		point = [coord[0], coord[1]]
		if coord[axis] > fold[1]: point[axis] = 2 * fold[1] - point[axis]
		if point not in tmp: tmp.append(point)

	if silver == None: silver = len(tmp)
	coords = tmp

output = []
for i in range(7): output.append([" "] * 41)
for coord in coords: output[coord[1]][coord[0]] = "#"

print(f"Silver: {silver}\nGold:")
for line in output[:-1]: print("".join(line))
