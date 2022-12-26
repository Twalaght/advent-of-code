#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

data = [[int(x) for x in line] for line in data]

lows = []
for i in range(len(data)):
	for j in range(len(data[i])):
		p = data[i][j]

		if i != 0:
			if data[i - 1][j] <= p: continue

		if i != len(data) - 1:
			if data[i + 1][j] <= p: continue

		if j != 0:
			if data[i][j - 1] <= p: continue

		if j != len(data[i]) - 1:
			if data[i][j + 1] <= p: continue


		lows.append(data[i][j])

silver = 0
for i in lows: silver += (i + 1)

print(f"Silver: {silver}")

def get_dir(i, j):
	p = data[i][j]

	best_val = 99
	coord = None

	if i != 0:
		if data[i - 1][j] <= p:
			if data[i - 1][j] < best_val:
				best_val = data[i - 1][j]
				coord = [i - 1, j]

	if i != len(data) - 1:
		if data[i + 1][j] <= p:
			if data[i + 1][j] < best_val:
				best_val = data[i + 1][j]
				coord = [i + 1, j]

	if j != 0:
		if data[i][j - 1] <= p:
			if data[i][j - 1] < best_val:
				best_val = data[i][j - 1]
				coord = [i, j - 1]

	if j != len(data[i]) - 1:
		if data[i][j + 1] <= p:
			if data[i][j + 1] < best_val:
				best_val = data[i][j + 1]
				coord = [i, j + 1]

	if coord is None: return True
	return coord

sinks = {}
for i in range(len(data)):
	for j in range(len(data[i])):
		if data[i][j] == 9:
			continue

		d = [i, j]
		coord = [i, j]

		while(True):
			d = get_dir(d[0], d[1])

			if d is True:
				break

			coord = d.copy()

		d_str = f"{coord[0]},{coord[1]}"
		if d_str in sinks:
			sinks[d_str] = sinks[d_str] + 1
		else:
			sinks[d_str] = 1

gold = []
for w in sorted(sinks, key=sinks.get, reverse=True):
	if (sinks[w] > 1):
		gold.append(sinks[w])

print(f"Gold: {gold[0] * gold[1] * gold[2]}")
