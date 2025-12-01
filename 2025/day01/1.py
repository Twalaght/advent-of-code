#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

dial, silver, gold = 50, 0, 0

for line in data:
    for i in range(int(line[1:])):
        dial = (dial + (1 if line[0] == "R" else -1)) % 100
        if dial == 0: gold += 1

    if dial == 0: silver += 1

print(f"Silver: {silver}\nGold: {gold}")
