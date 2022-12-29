#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read()

silver, gold = 0, 0
for i in range(len(data)):
	silver += 1 if data[i] == "(" else -1
	if gold == 0 and silver < 0: gold = i + 1

print(f"Silver: {silver}\nGold: {gold}")
