#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

poly = [char for char in data[0]]

rules, s_count, count, silver, gold = {}, {}, {}, {}, {}
for line in data[2:]:
	tmp = line.split(" -> ")
	rules[tmp[0]] = [f"{tmp[0][0]}{tmp[1]}", f"{tmp[1]}{tmp[0][1]}"]
	# count[tmp[0]], s_count[tmp[0]] = 0, 0
	# silver[tmp[1]], gold[tmp[1]] = 0, 0
	s_count[tmp[0]], count[tmp[0]] = 0, 0
	silver[tmp[1]], gold[tmp[1]] = 0, 0

for i in range(len(poly) - 1): count[f"{poly[i]}{poly[i + 1]}"] += 1

for loop in range(40):
	tmp = dict.fromkeys(count.keys(), 0)
	if loop == 10: s_count = count

	for pair in [x for x in count if count[x] != 0]:
		for new in rules[pair]: tmp[new] += count[pair]

	count = tmp

for entry in count:
	for char in entry:
		silver[char] += s_count[entry]
		gold[char] += count[entry]

for ends in [poly[0], poly[-1]]: silver[ends] += 1
for ends in [poly[0], poly[-1]]: gold[ends] += 1

for i in silver: silver[i] = silver[i] // 2
for i in gold: gold[i] = gold[i] // 2

silver = max(list(silver.values())) - min(list(silver.values()))
gold = max(list(gold.values())) - min(list(gold.values()))
print(f"Silver: {silver}\nGold: {gold}")
