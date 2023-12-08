#!/usr/bin/env python3

import sys
from math import lcm
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

path = {}
moves = data[0]
for line in data[2:]:
    source, dest = line.split(" = ")
    left, right = dest[1:-1].split(", ")
    path[source] = {"L": left, "R": right}

cycles = []
silver, gold = 0, 0
for pos in sorted([x for x in path if x.endswith("A")]):
    for i in range(int(1e7)):
        pos = path[pos][moves[i % len(moves)]]

        if pos == "ZZZ" and silver == 0:
            silver = i + 1

        if pos.endswith("Z"):
            cycles.append(i + 1)
            break

print(f"Silver: {silver}\nGold: {lcm(*cycles)}")
