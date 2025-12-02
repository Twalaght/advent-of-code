#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().strip().split(",")

def solve_silver(number: str) -> int:
    if number[len(number) // 2:] == number[:len(number) // 2]:
        return int(number)

    return 0

def solve_gold(number: str) -> int:
    for i in range(1, (len(number) // 2) + 1):
        target = number[:i]
        candidate = (len(number) // len(target)) * target
        if candidate == number:
            return int(number)

    return 0

silver, gold = 0, 0
for row in data:
    start, stop = [int(x) for x in row.split("-")]
    for i in range(start, stop + 1):
        silver += solve_silver(str(i))
        gold += solve_gold(str(i))

print(f"Silver: {silver}\nGold: {gold}")
