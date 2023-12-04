#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

numbers, symbols = [], []

for y, line in enumerate(data):
    buffer = ""
    for x, char in enumerate(line):
        if char.isnumeric():
            if not buffer: start = [y, x]
            buffer += char
        
        else:
            if char != ".": symbols.append((char, y, x))

            if buffer:
                numbers.append((int(buffer), start, [y, x - 1]))
                buffer = ""

    if buffer:
        numbers.append((int(buffer), start, [y, len(line) - 1]))
        buffer = ""

silver, gold = 0, 0
gears = {}
for number in numbers:
    part = False
    for y in range(number[1][0] - 1, number[2][0] + 2):
        y = max(0, min(len(data) - 1, y))

        for x in range(number[1][1] - 1, number[2][1] + 2):
            x = max(0, min(len(data[0]) - 1, x))

            if not data[y][x].isnumeric() and data[y][x] != ".":
                part = True
                if data[y][x] != "*": continue
                gears[(y, x)] = [number[0]] + gears.get((y, x), [])
    
    if part: silver += number[0]
    
for gear_set in [x for x in gears.values() if len(x) == 2]:
    gold += gear_set[0] * gear_set[1]

print(f"Silver: {silver}\nGold: {gold}")
