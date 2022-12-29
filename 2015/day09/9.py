#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

dists = {}
for line in data:
	tmp, cost = line.split(" = ")
	tmp = tmp.split(" to ")

	for i in range(2):
		if tmp[i] not in dists: dists[tmp[i]] = {}
		dists[tmp[i]][tmp[(i + 1) % 2]] = int(cost)

def visit(state, log, gold):
	log.append(state)
	if len(log) == len(dists): return 0
	best = 0 if gold else int(1e9)

	for opt in [loc for loc in dists[state] if loc not in log]:
		tmp = dists[state][opt] + visit(opt, log.copy(), gold)
		if gold and tmp > best or not gold and tmp < best: best = tmp

	return best

silver = min([visit(start, [], False) for start in dists])
gold = max([visit(start, [], True) for start in dists])
print(f"Silver: {silver}\nGold: {gold}")
