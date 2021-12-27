#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

nodes = {}
for i in data:
	n1, n2 = i.split("-")

	if n1 not in nodes:
		nodes[n1] = []

	if n2 not in nodes[n1]:
		nodes[n1].append(n2)

	if n2 not in nodes:
		nodes[n2] = []

	if n1 not in nodes[n2]:
		nodes[n2].append(n1)

for i in nodes:
	nodes[i].sort()

def travel(current, visited, dist, log):
	tmp = 0

	log.append(current)

	if current.islower():
		visited.append(current)

	options = nodes[current]

	for opt in options:
		if opt == "end":
			tmp += 1
			log.append("end")
			continue

		if opt not in visited:
			tmp += travel(opt, visited.copy(), dist + 1, log.copy())

	return tmp

visited = []
log = []
paths = travel("start", visited.copy(), 0, log.copy())

print(f"Silver: {paths}")

def p2(current, visited, log, spec):
	output = []
	log.append(current)

	if current.islower():
		visited.append(current)

	options = nodes[current]

	for opt in options:
		if opt == "end":
			log.append("end")
			output.append(log)
			continue

		if opt not in visited:
			tmp = p2(opt, visited.copy(), log.copy(), spec)
			output += tmp

		if opt in visited and spec == opt:
			tmp = p2(opt, visited.copy(), log.copy(), None)
			output += tmp

	return output

spec = []
for i in nodes:
	if i.islower() and i != "start" and i != "end":
		spec.append(i)

spec.sort()

paths = []

for s in spec:
	paths += p2("start", [], [], s)

for i in range(len(paths)):
	paths[i] = tuple(paths[i])

pset = set(paths)

print(f"Gold: {len(pset)}")
