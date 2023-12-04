#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

numbers = []
symbols = []

for y, line in enumerate(data):
    buffer = ""
    start = [-1, -1]
    end = [-1, -1]

    for x, char in enumerate(line):
        if char.isnumeric():
            if not buffer:
                start = [y, x]

            buffer += char
        
        else:
            if char != ".":
                symbols.append((char, y, x))

            if buffer:
                end = [y, x - 1]
                numbers.append((int(buffer), tuple(start), tuple(end)))
                buffer = ""

    if buffer:
        end = [y, len(line) - 1]
        numbers.append((int(buffer), tuple(start), tuple(end)))
        buffer = ""

silver = 0
gears = {}
for number in numbers:
    part = False
    for y in range(number[1][0] - 1, number[2][0] + 2):
        for x in range(number[1][1] - 1, number[2][1] + 2):
            y = max(0, y)
            y = min(len(data) - 1, y)
            x = max(0, x)
            x = min(len(data[0]) - 1, x)


            if not data[y][x].isnumeric() and data[y][x] != ".":
                part = True

                if data[y][x] == "*":
                    if (y, x) not in gears:
                        gears[(y, x)] = [number[0]]
                    else:
                        gears[(y, x)].append(number[0])
    
    if part:
        silver += number[0]
    
gold = 0
for gear_set in gears.values():
    if len(gear_set) == 2:
        gold += gear_set[0] * gear_set[1]

print(f"Silver: {silver}\nGold: {gold}")
