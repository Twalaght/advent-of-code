#!/usr/bin/env python3

import itertools
import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = [[x for x in line] for line in f.read().splitlines()]

x_gaps, y_gaps = [], []
for i in range(len(data[0])):
    if "#" not in [x[i] for x in data]: x_gaps.append(i)

for i in range(len(data)):
    if "#" not in data[i]: y_gaps.append(i)

galaxies = []
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "#": galaxies.append((y, x))

def distance(left: tuple, right: tuple, gold: bool) -> int:
    y_range, x_range = [range(min(left[i], right[i]), max(left[i], right[i])) for i in range(0, 2)]
    y_empty, x_empty = [[x for x in gaps if x in rng] for gaps, rng in zip([y_gaps, x_gaps], [y_range, x_range])]

    dist = abs(left[0] - right[0]) + abs(left[1] - right[1])
    return dist + (999999 if gold else 1) * (len(x_empty) + len(y_empty))

silver, gold = 0, 0
for pair in list(itertools.combinations(galaxies, 2)):
    silver += distance(*pair, False)
    gold += distance(*pair, True)

print(f"Silver: {silver}\nGold: {gold}")
