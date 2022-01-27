#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [int(x) for x in f.read().splitlines()]

silver = sum(data[i] < data[i + 1] for i in range(len(data) - 1))
gold = sum(data[i] < data[i + 3] for i in range(len(data) - 3))
print(f"Silver: {silver}\nGold: {gold}")
