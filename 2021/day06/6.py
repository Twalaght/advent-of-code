#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
		data = [int(x) for x in f.read().split(",")]

fish = [data.count(x) for x in range(9)]

for day in range(256):
	tmp = fish.pop(0)
	fish.append(tmp)
	fish[6] += tmp

	if day == 79: print(f"Silver: {sum(fish)}")
	if day == 255: print(f"Gold: {sum(fish)}")
