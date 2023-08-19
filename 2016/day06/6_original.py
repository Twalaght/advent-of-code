#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

data = [[x[i] for x in data] for i in range(8)]

mode = lambda string: max(set(string), key=string.count)
inv_mode = lambda string: min(set(string), key=string.count)

silver = "".join([mode(x) for x in data])
gold = "".join([inv_mode(x) for x in data])

print(f"Silver: {silver}\nGold: {gold}")
