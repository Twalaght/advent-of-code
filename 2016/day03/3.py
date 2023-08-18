#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	silver_input = [list(map(int, x.split())) for x in f.read().splitlines()]

data = []
for i in range(3):
	for x in silver_input: data.append(x[i])

gold_input = [data[i : i + 3] for i in range(0, len(data), 3)] 

valid = lambda lengths: 1 if lengths[0] + lengths[1] > lengths[2] else 0

silver, gold = 0, 0
for triangle in silver_input: silver += valid(sorted(triangle))
for triangle in gold_input: gold += valid(sorted(triangle))

print(f"Silver: {silver}\nGold: {gold}")
