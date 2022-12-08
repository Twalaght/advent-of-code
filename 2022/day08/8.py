#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [[int(t) for t in x] for x in f.read().splitlines()]

def visible(view, val):
	return all(x < int(val) for x in view)

def scenic(view, val):
	score = 0
	for x in view:
		score += 1
		if x >= int(val): break

	return score

length = len(data[0])
silver, gold = 2 * (len(data) + length - 2), 0
for y in range(1, len(data) - 1):
	for x in range(1, length - 1):
		val = data[y][x]
		l = [data[y][i] for i in range(0, x)]
		r = [data[y][i] for i in range(x + 1, length)]
		t = [data[i][x] for i in range(0, y)]
		b = [data[i][x] for i in range(y + 1, len(data))]

		if any([visible(x, val) for x in [l, r, t, b]]): silver += 1

		score = 1
		for x in [l[::-1], r, t[::-1], b]: score *= scenic(x, val)
		if score > gold: gold = score

print(f"Silver: {silver}\nGold: {gold}")
