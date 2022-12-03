#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

silver, gold = 0, 0
for line in data:
	# Get the common element and add the priority value
	left = [x for x in line[:len(line) // 2]]
	right = [x for x in line[len(line) // 2:]]
	comb = list(set(left).intersection(right))[0]
	silver += ord(comb) - (96 if comb.islower() else 38)

for i in range(0, len(data), 3):
	# Get common element for groups of 3 and add the priority value
	comb = list(set(data[i]).intersection(data[i + 1]).intersection(data[i + 2]))[0]
	gold += ord(comb) - (96 if comb.islower() else 38)

print(f"Silver: {silver}\nGold: {gold}")
