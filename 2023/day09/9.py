#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = [[int(x) for x in line.split()] for line in f.read().splitlines()]

silver, gold = 0, 0
for line in data:
    rows = [line]

    while True:
        rows.append([right - left for left, right in zip(rows[-1][:-1], rows[-1][1:])])
        if not any(rows[-1]): break

    for i, row in enumerate(rows):
        silver += row[-1]
        gold += row[0] if i % 2 == 0 else -row[0]
    
print(f"Silver: {silver}\nGold: {gold}")
