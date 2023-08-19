#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.replace("]", "[").split("[") for x in f.read().splitlines()]

def tls(segment):
	groups = [tuple(segment[i : i + 4]) for i in range(len(segment) - 3)]
	return any([(x[0] == x[3] and x[1] == x[2] and x[0] != x[1]) for x in groups])

def ssl(segment):
	groups = [tuple(segment[i : i + 3]) for i in range(len(segment) - 2)]
	return [x for x in groups if x[0] == x[2]]

silver, gold = 0, 0
for line in data:
	abba = None
	bab = {"outside": [], "inside": []}

	for i, segment in enumerate(line):
		if res := tls(segment):
			if (True if i % 2 else (abba == None)): abba = (not res if i % 2 else res)

		bab["inside" if i % 2 else "outside"] += ssl(segment)

	if abba: silver += 1

	while bab["outside"]:
		inverse = lambda x: (x[1], x[0], x[1])
		if inverse(bab["outside"].pop()) in bab["inside"]:
			gold += 1
			break

print(f"Silver: {silver}\nGold: {gold}")
