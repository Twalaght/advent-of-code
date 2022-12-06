#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()][0]

def solve(data, window):
	for i in range(len(data) - window):
		if len(set(data[i:i + window])) == window:
			return i + window

silver, gold = solve(data, 4), solve(data, 14)
print(f"Silver: {silver}\nGold: {gold}")
