#!/usr/bin/env python3

import itertools
import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = [[x for x in line] for line in f.read().splitlines()]

x_gaps = []
y_gaps = []

for i in range(len(data[0])):
    test = [x[i] for x in data]
    if "#" not in test:
        x_gaps.append(i)

for i in range(len(data)):
    test = data[i]
    if "#" not in test:
        y_gaps.append(i)

galaxies = []
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "#":
            galaxies.append((y, x))

def distance(left: tuple, right: tuple, gold: bool) -> int:
    x_range = range(min(left[1], right[1]) + 1, max(left[1], right[1]))
    y_range = range(min(left[0], right[0]) + 1, max(left[0], right[0]))

    x_empty = [x for x in x_gaps if x in x_range]
    y_empty = [x for x in y_gaps if x in y_range]

    dist = abs(left[0] - right[0]) + abs(left[1] - right[1])
    if gold:
        dist += 999999 * (len(x_empty) + len(y_empty))
    else:
        dist += len(x_empty) + len(y_empty)

    return dist

silver, gold = 0, 0
for pair in list(itertools.combinations(galaxies, 2)):
    silver += distance(*pair, False)
    gold += distance(*pair, True)

print(f"Silver: {silver}\nGold: {gold}")
