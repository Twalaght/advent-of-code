#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

for x in data: print(x)

# print(f"Silver: {silver}\nGold: {gold}")
