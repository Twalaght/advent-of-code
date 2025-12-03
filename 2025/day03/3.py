#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

def solve(row: str, depth: int) -> str:
    for left in [str(x) for x in range(9, 0, -1)]:
        if left not in row:
            continue

        if depth <= 1:
            return left

        if not (substr := row[row.index(left) + 1:]):
            continue

        if (ans := solve(substr, depth - 1)):
            return f"{left}{ans}"

    return None

silver, gold = 0, 0
for row in data:
    silver += int(solve(row, 2))
    gold += int(solve(row, 12))

print(f"Silver: {silver}\nGold: {gold}")
