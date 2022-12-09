#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.split() for x in f.read().splitlines()]

silver, gold = set(), set()

h = [0, 0]
t = [0, 0]
for move in data:
	move[1] = int(move[1])

	for _ in range(move[1]):
		if move[0] == "L": h[0] -= 1
		if move[0] == "R": h[0] += 1
		if move[0] == "U": h[1] += 1
		if move[0] == "D": h[1] -= 1

		# If we need to move diagonaly
		if h[0] != t[0] and h[1] != t[1]:
			if abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1:
				if h[0] > t[0]: t[0] += 1
				if h[0] < t[0]: t[0] -= 1

				if h[1] > t[1]: t[1] += 1
				if h[1] < t[1]: t[1] -= 1

		# Linear move
		else:
			if abs(h[0] - t[0]) > 1:
				if h[0] > t[0]: t[0] += 1
				if h[0] < t[0]: t[0] -= 1

			if abs(h[1] - t[1]) > 1:
				if h[1] > t[1]: t[1] += 1
				if h[1] < t[1]: t[1] -= 1

		silver.add(tuple(t))

rope = []
for _ in range(10): rope.append([0, 0])

for move in data:
	move[1] = int(move[1])

	for _ in range(move[1]):

		if move[0] == "L": rope[0][0] -= 1
		if move[0] == "R": rope[0][0] += 1
		if move[0] == "U": rope[0][1] += 1
		if move[0] == "D": rope[0][1] -= 1

		for i in range(1, len(rope)):
			# If we need to move diagonaly
			if rope[i - 1][0] != rope[i][0] and rope[i - 1][1] != rope[i][1]:
				if abs(rope[i - 1][0] - rope[i][0]) > 1 or abs(rope[i - 1][1] - rope[i][1]) > 1:
					if rope[i - 1][0] > rope[i][0]: rope[i][0] += 1
					if rope[i - 1][0] < rope[i][0]: rope[i][0] -= 1

					if rope[i - 1][1] > rope[i][1]: rope[i][1] += 1
					if rope[i - 1][1] < rope[i][1]: rope[i][1] -= 1

			# Linear move
			else:
				if abs(rope[i - 1][0] - rope[i][0]) > 1:
					if rope[i - 1][0] > rope[i][0]: rope[i][0] += 1
					if rope[i - 1][0] < rope[i][0]: rope[i][0] -= 1

				if abs(rope[i - 1][1] - rope[i][1]) > 1:
					if rope[i - 1][1] > rope[i][1]: rope[i][1] += 1
					if rope[i - 1][1] < rope[i][1]: rope[i][1] -= 1

		gold.add(tuple(rope[-1]))

silver, gold = len(silver), len(gold)
print(f"Silver: {silver}\nGold: {gold}")
