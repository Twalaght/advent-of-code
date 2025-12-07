#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

silver, gold = 0, 0
for _ in range(100):
    for y in range(len(data)):
        for x in range(len(data[0])):
            count = 0

            if data[y][x] != "@":
                continue

            for y_move in (-1, 0, 1):
                for x_move in (-1, 0, 1):
                    new_y = y + y_move
                    new_x = x + x_move
                    
                    if y_move == 0 and x_move == 0:
                        continue

                    if new_y < 0 or new_y >= len(data):
                        continue

                    if new_x < 0 or new_x >= len(data[0]):
                        continue

                    target = data[y + y_move][x + x_move]
                    if target == "@":
                        count += 1
            
            if count <= 3:
                if _ == 0:
                    silver += 1
                else:
                    tmp = [p for p in data[y]]
                    tmp[x] = "."
                    data[y] = "".join(tmp)
                    gold += 1

print(f"Silver: {silver}\nGold: {gold}")
