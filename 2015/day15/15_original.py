#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.split() for x in f.read().splitlines()]

data = [(int(x[2][:-1]), int(x[4][:-1]), int(x[6][:-1]), int(x[8][:-1]), int(x[-1])) for x in data]

limit = 100
silver = 0
gold = 0
for i in range(limit + 1):
	for j in range(limit + 1 - i):
		for k in range(limit + 1 - i - j):
			l = limit - (i + j + k)

			cap = (i * data[0][0]) + (j * data[1][0]) + (k * data[2][0]) + (l * data[3][0])
			dur = (i * data[0][1]) + (j * data[1][1]) + (k * data[2][1]) + (l * data[3][1])
			fla = (i * data[0][2]) + (j * data[1][2]) + (k * data[2][2]) + (l * data[3][2])
			tex = (i * data[0][3]) + (j * data[1][3]) + (k * data[2][3]) + (l * data[3][3])
			cal = (i * data[0][4]) + (j * data[1][4]) + (k * data[2][4]) + (l * data[3][4])

			if cap <= 0 or dur <= 0 or fla <= 0 or tex <= 0: continue

			score = cap * dur * fla * tex

			if score > silver: silver = score
			if score > gold and cal == 500: gold = score

print(f"Silver: {silver}\nGold: {gold}")
