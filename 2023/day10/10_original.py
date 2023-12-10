#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

for y, row in enumerate(data):
    if "S" in row:
        pos = (y, row.index("S"))

def translate(pos: tuple[int], direction: str) -> tuple[tuple[int], str]:
    new_pos = list(pos)
    if direction == "N":
        new_pos = [new_pos[0] - 1, new_pos[1]]

    elif direction == "E":
        new_pos = [new_pos[0], new_pos[1] + 1]

    elif direction == "S":
        new_pos = [new_pos[0] + 1, new_pos[1]]

    elif direction == "W":
        new_pos = [new_pos[0], new_pos[1] - 1]

    tile = data[new_pos[0]][new_pos[1]]
    if tile == "|":
        if direction == "S" or direction == "N":
            return tuple(new_pos), direction

    if tile == "-":
        if direction == "E" or direction == "W":
            return tuple(new_pos), direction

    if tile == "L":
        if direction == "S":
            return tuple(new_pos), "E"
        
        if direction == "W":
            return tuple(new_pos), "N"

    if tile == "J":
        if direction == "S":
            return tuple(new_pos), "W"
        
        if direction == "E":
            return tuple(new_pos), "N"

    if tile == "7":
        if direction == "N":
            return tuple(new_pos), "W"
        
        if direction == "E":
            return tuple(new_pos), "S"

    if tile == "F":
        if direction == "N":
            return tuple(new_pos), "E"
        
        if direction == "W":
            return tuple(new_pos), "S"
    
    if tile == "S":
        return "DONE"
    
    return None

positions = [pos]
dirs = ["N", "S", "E", "W"]
dirs = {d: translate(pos, d) for d in dirs if translate(pos, d)}
direction = list(dirs.keys())[0]
north = ("|", "L", "J", "S") if direction in ("S", "N") else ("|", "L", "J")


while True:
    output = translate(pos, direction)

    if output == "DONE":
        break

    new_pos, new_dir = output
    positions.append(new_pos)
    pos = new_pos
    direction = new_dir

silver = len(positions) // 2

gold = 0
for y in range(len(data)):
    north_facing = 0
    for x in range(len(data[0])):
        if (y, x) in positions:
            if data[y][x] in north:
                north_facing += 1
        
        else:
            if north_facing % 2 == 1:
                gold += 1

print(f"Silver: {silver}\nGold: {gold}")
