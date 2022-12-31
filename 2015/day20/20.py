#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	target = int(f.read().strip())

def solve(target, multiplier, limit):
	# Only check up to target // multiplier, no need to go past
	d = target // multiplier
	counts = [0 for _ in range(d)]

	for i in range(1, d):
		# Cap out at limit if elves stop delivering
		for j in range(1, min(d // i, limit)):
			# Add each elves contribution
			counts[j * i - 1] += i * multiplier

		if counts[i - 1] >= target: return i

silver, gold = solve(target, 10, target), solve(target, 11, 50)
print(f"Silver: {silver}\nGold: {gold}")
