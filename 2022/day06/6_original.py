#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()][0]

for i in range(len(data)):
	tmp = []
	for char in range(4):
		tmp.append(data[i + char])

	tmp = set(tmp)
	if len(tmp) == 4:
		silver = i + 4
		break

for i in range(len(data)):
	tmp = []
	for char in range(14):
		tmp.append(data[i + char])

	tmp = set(tmp)
	if len(tmp) == 14:
		gold = i + 14
		break

print(f"Silver: {silver}\nGold: {gold}")
