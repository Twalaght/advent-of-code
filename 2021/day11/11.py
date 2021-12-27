#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [[int(char) for char in x] for x in f.read().splitlines()]

def flash(x, y):
	for i in [-1, 0, 1]:
		if x + i < 0 or x + i > 9: continue
		for j in [-1, 0, 1]:
			if y + j < 0 or y + j > 9: continue
			data[x + i][y + j] += 1

	data[x][y] = -99

silver = 0
for step in range(1000):
	if step == 100: print(f"Silver: {silver}")

	if all(not x for row in data for x in row):
		print(f"Gold: {step}")
		break

	data = [[x + 1 for x in row] for row in data]

	while (True):
		flashed = False
		for x in range(10):
			for y in range(10):
				if data[x][y] > 9:
					flash(x, y)
					silver += 1
					flashed = True

		if not flashed: break

	data = [[0 if x < 0 else x for x in row] for row in data]
