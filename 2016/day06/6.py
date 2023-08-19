#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

data = [[x[i] for x in data] for i in range(8)]
mode = lambda string, gold: (min if gold else max)(set(string), key=string.count)
password = lambda data, gold: "".join([mode(x, gold) for x in data])

print(f"Silver: {password(data, False)}\nGold: {password(data, True)}")
