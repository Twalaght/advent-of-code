#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
		data = [int(x) for x in f.read().split(",")]

data.sort()
median = data[len(data) // 2]
silver = sum(abs(x - median) for x in data)
average = sum(data) // len(data)
gold = sum((abs(x - average) * (abs(x - average) + 1) // 2) for x in data)
print(f"Silver: {silver}\nGold: {gold}")
