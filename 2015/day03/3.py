#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read()]

ins = {"^": [1, 1], ">": [0, 1], "v": [1, -1], "<": [0, -1]}

santa = [0, 0]
silver, gold = {tuple(santa)}, {tuple(santa)}
pair = [[0, 0], [0, 0]]

for i in range(len(data)):
	cmd = data[i]
	pair[i % 2][ins[cmd][0]] += ins[cmd][1]
	santa[ins[cmd][0]] += ins[cmd][1]

	silver.add(tuple(santa))
	for i in pair: gold.add(tuple(i))

print(f"Silver: {len(silver)}\nGold: {len(gold)}")
