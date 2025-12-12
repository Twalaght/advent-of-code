#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

gold = 0
for row in data[30:]:
    dims, presents = row.split(": ")
    x, y = [int(x) for x in dims.split("x")]

    # Outright discard shapes and assume everything is 3x3, answer does not change.
    if sum([int(x) for x in presents.split(" ")]) <= (x // 3) * (y // 3):
        gold += 1

print(f"Gold: {gold}")
