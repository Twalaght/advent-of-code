#!/usr/bin/env python3

import sys
from math import lcm
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

moves = data[0]

path = {}
for line in data[2:]:
    source, dest = line.split(" = ")
    left, right = dest[1:-1].split(", ")
    
    path[source] = {"L": left, "R": right}

silver = 0
pos = "AAA"
for i in range(int(1e7)):
    index = i % len(moves)
    
    pos = path[pos][moves[index]]

    if pos == "ZZZ":
        silver = i + 1
        break

positions = [x for x in path if x.endswith("A")]
cycles = []
gold = 0
for pos in positions:
    start = -1
    for i in range(int(1e7)):
        index = i % len(moves)
        
        pos = path[pos][moves[index]]

        if pos.endswith("Z"):
            if start == -1:
                start = i + 1
            else:
                cycles.append(start)
                break

gold = lcm(*cycles)
print(f"Silver: {silver}\nGold: {gold}")
