#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

tmp = 0
elves = []

for line in data:
	if line:
		tmp += int(line)
	else:
		elves.append(tmp)
		tmp = 0

silver = max(elves)

elves.sort()
elves = elves[-3:]
gold = sum(elves)

print(f"Silver: {silver}\nGold: {gold}")
