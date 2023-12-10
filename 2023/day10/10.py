#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

pos = [(y, row.index("S")) for y, row in enumerate(data) if "S" in row ][0]

def translate(pos: tuple[int], direction: str) -> tuple[tuple[int], str]:
    new_pos = list(pos)

    if direction == "N": new_pos = [pos[0] - 1, pos[1]]
    if direction == "E": new_pos = [pos[0], pos[1] + 1]
    if direction == "S": new_pos = [pos[0] + 1, pos[1]]
    if direction == "W": new_pos = [pos[0], pos[1] - 1]

    tile = data[new_pos[0]][new_pos[1]]
    if tile == "|" and direction in ("N", "S"): return tuple(new_pos), direction
    if tile == "-" and direction in ("E", "W"): return tuple(new_pos), direction
    if tile == "L":
        if direction == "S": return tuple(new_pos), "E"
        if direction == "W": return tuple(new_pos), "N"
    if tile == "J":
        if direction == "S": return tuple(new_pos), "W"
        if direction == "E": return tuple(new_pos), "N"
    if tile == "7":
        if direction == "N": return tuple(new_pos), "W"
        if direction == "E": return tuple(new_pos), "S"
    if tile == "F":
        if direction == "N": return tuple(new_pos), "E"
        if direction == "W": return tuple(new_pos), "S"

    return None

dirs = {d: translate(pos, d) for d in ("N", "S", "E", "W") if translate(pos, d)}
direction = list(dirs.keys())[0]
north = ["|", "L", "J"] + ["S"] if direction in ("S", "N") else []

positions = [pos]
while True:
    if not (output := translate(pos, direction)): break
    pos, direction = output
    positions.append(pos)

gold = 0
for y in range(len(data)):
    north_facing = 0
    for x in range(len(data[0])):
        if (y, x) in positions:
            if data[y][x] in north: north_facing += 1
        else:
            if north_facing % 2 == 1: gold += 1

print(f"Silver: {len(positions) // 2}\nGold: {gold}")
