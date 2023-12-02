#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = [x.split(": ")[-1] for x in f.read().splitlines()]

data = [[[[pair for pair in
        x.split(" ") if pair] for x in
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
    maxes = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for hand in game:
        for pair in hand:
            if int(pair[0]) > limits[pair[-1]]:
                valid = False

            maxes[pair[-1]] = max(maxes[pair[-1]], int(pair[0]))

    if valid:
        silver += i

    power = maxes["red"] * maxes["green"] * maxes["blue"]
    gold += power

print(f"Silver: {silver}\nGold: {gold}")
