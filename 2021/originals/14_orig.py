#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

poly = [char for char in data[0]]

rules = {}
for line in data[2:]:
	tmp = line.split(" -> ")
	rules[tmp[0]] = tmp[1]

for l in range(10):
	new = []
	for i in range(len(poly) - 1):
		tmp = f"{poly[i]}{poly[i + 1]}"

		if tmp in rules:
			new.append(poly[i])
			new.append(rules[tmp])
		else:
			new.append(poly[i])

	new.append(poly[-1])
	poly = new

max = 0
min = int(1e9)
for i in set(poly):
	tmp = poly.count(i)
	if tmp > max: max = tmp
	if tmp < min: min = tmp

print(f"Silver: {max - min}")


poly = [char for char in data[0]]
count = {}
rules = {}
for line in data[2:]:
	tmp = line.split(" -> ")
	rules[tmp[0]] = [f"{tmp[0][0]}{tmp[1]}", f"{tmp[1]}{tmp[0][1]}"]
	count[tmp[0]] = 0

for i in range(len(poly) - 1):
	tmp = f"{poly[i]}{poly[i + 1]}"
	count[tmp] += 1

for _ in range(40):
	tmp = {}

	for c in count:
		if count[c] == 0: continue

		res = rules[c]

		for r in res:
			if r not in tmp:
				tmp[r] = count[c]
			else:
				tmp[r] += count[c]

	count = tmp.copy()

total = {}
for c in count:
	if c[0] not in total:
		total[c[0]] = count[c]
	else:
		total[c[0]] += count[c]

	if c[1] not in total:
		total[c[1]] = count[c]
	else:
		total[c[1]] += count[c]

for i in [poly[0], poly[-1]]:
	total[i] += 1

for i in total:
	total[i] = int(total[i] / 2)

max = 0
min = int(1e20)
for i in total:
	if total[i] > max: max = total[i]
	if total[i] < min: min = total[i]

print(f"Gold: {max - min}")
