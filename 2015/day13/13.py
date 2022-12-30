#!/usr/bin/python3

import sys
import itertools
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.split() for x in f.read().splitlines()]

names = set([x[0] for x in data] + ["you"])
happy = {}
for name in names:
	lines = [x for x in data if x[0] == name]
	tmp = {}
	for line in lines:
		tmp[line[-1][:-1]] = (1 if line[2] == "gain" else -1) * int(line[3])

	happy[name] = tmp

silver, gold = 0, 0
for seats in list(itertools.permutations(names)):
	s_joy, g_joy = 0, 0
	for p in range(len(seats)):
		if seats[p] == "you": continue

		left, right = (p - 1) % len(seats), (p + 1) % len(seats)

		if seats[left] != "you": g_joy += happy[seats[p]][seats[left]]
		if seats[right] != "you": g_joy += happy[seats[p]][seats[right]]

		if seats[left] == "you": left = (left - 1) % len(seats)
		if seats[right] == "you": right = (right + 1) % len(seats)
		s_joy += happy[seats[p]][seats[left]]
		s_joy += happy[seats[p]][seats[right]]

	silver, gold = max(silver, s_joy), max(gold, g_joy)

print(f"Silver: {silver}\nGold: {gold}")
