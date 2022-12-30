#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.replace(",", "").replace(":", "").split(" ") for x in f.read().splitlines()]

sues = []
for line in data:
	tmp = {}
	tmp[line[0]] = int(line[1])
	tmp[line[2]] = int(line[3])
	tmp[line[4]] = int(line[5])
	tmp[line[6]] = int(line[7])
	sues.append(tmp)

known = {"children": 3,
		"cats": 7,
		"samoyeds": 2,
		"pomeranians": 3,
		"akitas": 0,
		"vizslas": 0,
		"goldfish": 5,
		"trees": 3,
		"cars": 2,
		"perfumes": 1}

silver = 0
gold = 0
for sue in sues:
	s_valid = True
	g_valid = True
	for k in known:
		if k not in sue: continue
		if known[k] != sue[k]: s_valid = False

		if k in ["cats", "trees"]:
			if known[k] >= sue[k]: g_valid = False

		elif k in ["pomeranians", "goldfish"]:
			if known[k] <= sue[k]: g_valid = False

		else:
			if known[k] != sue[k]: g_valid = False

	if s_valid: silver = sue["Sue"]
	if g_valid: gold = sue["Sue"]

print(f"Silver: {silver}\nGold: {gold}")
