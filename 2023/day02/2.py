#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = [x.split(": ")[-1] for x in f.read().splitlines()]

data = [[[list(filter(None, x.split(" "))) for x in
          showing.split(",")]
          for showing in line.split(";")]
          for line in data]

limits = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

silver, gold = 0, 0
for i, game in enumerate(data, 1):
    valid = True
    maxes = {k: 0 for k in limits.keys()}

    for pair in [pair for showing in game for pair in showing]:
        if int(pair[0]) > limits[pair[-1]]: valid = False
        maxes[pair[-1]] = max(maxes[pair[-1]], int(pair[0]))

    if valid: silver += i

    tmp = 1
    for power in maxes.values(): tmp *= power
    gold += tmp

print(f"Silver: {silver}\nGold: {gold}")
