#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

silver, gold = 0, 0
for loop in range(1000):
    moved = False
    for y in range(len(data)):
        for x in range(len(data[0])):
            count = 0

            if data[y][x] != "@":
                continue

            for new_y in (y + m for m in (-1, 0, 1)):
                for new_x in (x + m for m in (-1, 0, 1)):
                    if (
                        (new_y == y and new_x == x) or
                        (new_y < 0 or new_y >= len(data)) or
                        (new_x < 0 or new_x >= len(data[0]))
                    ):
                        continue

                    if data[new_y][new_x] == "@":
                        count += 1
            
            if count < 4:
                moved = True
                if loop == 0:
                    silver += 1
                else:
                    data[y] = "".join([(data[y][i] if i != x else ".") for i in range(len(data[y]))])
                    gold += 1
    
    if not moved:
        break

print(f"Silver: {silver}\nGold: {gold}")
