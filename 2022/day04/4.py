#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.split(",") for x in f.read().splitlines()]

def get_range(task):
	return set(range(int(task.split("-")[0]), int(task.split("-")[1]) + 1))

silver, gold = 0, 0
for line in data:
	left, right = get_range(line[0]), get_range(line[1])
	if left.issubset(right) or right.issubset(left): silver += 1
	if left.intersection(right) or right.intersection(left): gold += 1

print(f"Silver: {silver}\nGold: {gold}")
