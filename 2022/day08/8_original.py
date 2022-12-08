#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

def validate(strip, val):
	tmp = [int(x) for x in strip]
	res = all(x < int(val) for x in tmp)
	return res

def scenic(strip, val):
	tmp = [int(x) for x in strip]

	score = 0
	for x in tmp:
		if x < int(val):
			score += 1
		else:
			score += 1
			break

	return score

length = len(data[0])
silver = 2 * length + (2 * len(data)) - 4
for y in range(1, len(data) - 1):
	for x in range(1, length - 1):
		left = [data[y][i] for i in range(0, x)]
		right = [data[y][i] for i in range(x + 1, length)]
		top = [data[i][x] for i in range(0, y)]
		btm = [data[i][x] for i in range(y + 1, len(data))]

		val = data[y][x]

		if validate(left, val) or validate(right, val) or validate(top, val) or validate(btm, val):
			silver += 1

gold = 0
for y in range(1, len(data) - 1):
	for x in range(1, length - 1):
		left = [data[y][i] for i in range(0, x)][::-1]
		right = [data[y][i] for i in range(x + 1, length)]
		top = [data[i][x] for i in range(0, y)][::-1]
		btm = [data[i][x] for i in range(y + 1, len(data))]

		val = data[y][x]

		tmp = scenic(left, val) * scenic(right, val) * scenic(top, val) * scenic(btm, val)

		if tmp > gold: gold = tmp

print(f"Silver: {silver}\nGold: {gold}")
