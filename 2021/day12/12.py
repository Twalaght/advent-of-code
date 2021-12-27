#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

nodes = {}
for link in data:
	left, right = link.split("-")
	if left not in nodes: nodes[left] = []
	if right not in nodes: nodes[right] = []
	if left not in nodes[right]: nodes[right].append(left)
	if right not in nodes[left]: nodes[left].append(right)

for i in nodes: nodes[i].sort()

def travel(current, visited, log, special):
	log.append(current)
	if current.islower(): visited.append(current)

	output = []
	for opt in nodes[current]:
		if opt == "end":
			output.append(log)

		elif opt not in visited:
			output += travel(opt, visited.copy(), log.copy(), special)

		elif opt in visited and special == opt:
			output += travel(opt, visited.copy(), log.copy(), None)

	return output

silver = travel("start", [], [], None)

gold = set()
for small in sorted([n for n in nodes if n.islower() and n not in ["start", "end"]]):
	for path in travel("start", [], [], small): gold.add(tuple(path))

print(f"Silver {len(silver)}\nGold: {len(gold)}")
