#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

gamma, epsilon = "", ""
for i in range(12):
	count = sum([(1 if x[i] == "1" else -1) for x in data])
	gamma += "1" if count > 0 else "0"
	epsilon += "1" if count < 0 else "0"

def rating(data, bmap):
	for i in range(12):
		count = sum([(1 if x[i] == "1" else -1) for x in data])
		cpy_bit = bmap[0] if count >= 0 else bmap[1]
		data = [entry for entry in data if entry[i] == cpy_bit]

		if len(data) == 1: return int(data[0], 2)

silver = int(gamma, 2) * int(epsilon, 2)
gold = rating(data, ["0", "1"]) * rating(data, ["1", "0"])
print(f"Silver: {silver}\nGold: {gold}")
