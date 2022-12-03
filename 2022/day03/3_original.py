#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

silver = 0
for line in data:
	left = [x for x in line[:len(line) // 2]]
	right = [x for x in line[len(line) // 2:]]
	comb = list(set(left).intersection(right))

	for i, val in enumerate(comb):
		if val.islower():
			comb[i] = ord(val) - 96
		else:
			comb[i] = ord(val) - 38

		silver += comb[i]

gold = 0
for i in range(0, len(data), 3):
	# print(i)
	one = data[i]
	two = data[i + 1]
	three = data[i + 2]
	comb = list(set(one).intersection(two))
	comb = list(set(comb).intersection(three))

	for i, val in enumerate(comb):
		if val.islower():
			comb[i] = ord(val) - 96
		else:
			comb[i] = ord(val) - 38

		gold += comb[i]

print(f"Silver: {silver}\nGold: {gold}")
