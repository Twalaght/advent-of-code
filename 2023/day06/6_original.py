#!/usr/bin/env python3

import math
import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

times = [int(x) for x in data[0].split()[1:]]
dists = [int(x) for x in data[1].split()[1:]]
last_race_time = int("".join([str(x) for x in times]))
last_race_dist = int("".join([str(x) for x in dists]))

times.append(last_race_time)
dists.append(last_race_dist)

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
