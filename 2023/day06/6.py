#!/usr/bin/env python3

import math
import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

parse = lambda line: [int(x) for x in line.split()[1:]] + [int("".join(line.split()[1:]))]
times, dists = parse(data[0]), parse(data[1])

silver = 1
for i, (time, dist) in enumerate(zip(times, dists)):
    square_root = math.sqrt(pow(time, 2) - (4 * (dist + 1)))
    lower = math.ceil(-(-time + square_root) / 2)
    upper = math.floor(-(-time - square_root) / 2)
    num_wins = upper - lower + 1

    if i != len(times) - 1:
        silver *= num_wins
    else:
        gold = num_wins

print(f"Silver: {silver}\nGold: {gold}")
