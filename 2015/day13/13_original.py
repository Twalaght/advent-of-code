#!/usr/bin/python3

import sys
import itertools
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.split() for x in f.read().splitlines()]

names = set([x[0] for x in data])
happy = {}

for name in names:
	lines = [x for x in data if x[0] == name]

	tmp = {}
	for line in lines:
		value = int(line[3]) if line[2] == "gain" else -1 * int(line[3])
		tmp[line[-1][:-1]] = value

	happy[name] = tmp

silver = 0
for seats in list(itertools.permutations(names)):
	joy = 0
	for p in range(len(seats)):
		left = (p - 1) % len(seats)
		right = (p + 1) % len(seats)
		joy += happy[seats[p]][seats[left]]
		joy += happy[seats[p]][seats[right]]

	silver = max(silver, joy)

gold = 0
names.add("you")
for seats in list(itertools.permutations(names)):
	joy = 0
	for p in range(len(seats)):
		if seats[p] == "you": continue

		left = (p - 1) % len(seats)
		right = (p + 1) % len(seats)

		if seats[left] != "you":
			joy += happy[seats[p]][seats[left]]
		if seats[right] != "you":
			joy += happy[seats[p]][seats[right]]

	gold = max(gold, joy)

print(f"Silver: {silver}\nGold: {gold}")
