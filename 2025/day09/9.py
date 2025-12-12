#!/usr/bin/env python3

import sys
from typing import NamedTuple
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

class Tile(NamedTuple):
    x: int
    y: int

tiles = [Tile(*[int(x) for x in coord.split(",")]) for coord in data]

def rectangle(a: Tile, b: Tile) -> int:
    return (abs(a.x - b.x) + 1) * (abs(a.y - b.y) + 1)

def padded_translate_series(tiles: list[Tile]) -> tuple[list[int], list[int]]:
    output = [[-1], [-1]]
    for i, attr in enumerate(["x", "y"]):
        tmp_sorted = sorted({getattr(t, attr) for t in tiles})
        for item in tmp_sorted:
            output[i].append(item)
            output[i].append(-1)

    return tuple(output)

sorted_x, sorted_y = padded_translate_series(tiles)

line = ["@" for _ in range(len(sorted_x))]
mapping = [line.copy() for _ in range(len(sorted_y))]

def translate(in_tile: Tile) -> Tile:
    return Tile(x=sorted_x.index(in_tile.x), y=sorted_y.index(in_tile.y))

# Fill in the lines between tiles.
last_tile = translate(tiles[-1])
for i, og_tile in enumerate(tiles, start=1):
    tile = translate(og_tile)

    x = last_tile.x
    y = last_tile.y

    dx = 0 if tile.x == last_tile.x else -int((last_tile.x - tile.x) / abs(last_tile.x - tile.x))
    dy = 0 if tile.y == last_tile.y else -int((last_tile.y - tile.y) / abs(last_tile.y - tile.y))

    while (x != tile.x or y != tile.y):
        x += dx
        y += dy
        mapping[y][x] = "#"
    
    last_tile = tile

flooded = set()
flood_targets = [(0, 0)]
def flood(x: int, y: int) -> None:
    flooded.add((x, y))

    if mapping[y][x] == "#" or mapping[y][x] == ".":
        return

    if mapping[y][x] == "@":
        mapping[y][x] = "."

    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dy == 0 and dx == 0:
                continue

            if 0 <= (new_x := x + dx) < len(mapping[0]):
                flood_targets.append((new_x, y))
            if 0 <= (new_y := y + dy) < len(mapping):
                flood_targets.append((x, new_y))
            
while flood_targets:
    for target in (flood_targets := [x for x in flood_targets if x not in flooded]):
        flood(*target)

for y in range(len(mapping)):
    for x in range(len(mapping[y])):
        if mapping[y][x] == "@":
            mapping[y][x] = "#"

def check_gold(a: Tile, b: Tile) -> bool:
    trans_a, trans_b = translate(a), translate(b)
    for row in mapping[min(trans_a.y, trans_b.y):max(trans_a.y, trans_b.y) + 1]:
        if "." in row[min(trans_a.x, trans_b.x):max(trans_a.x, trans_b.x) + 1]:
            return False

    return True

silver, gold = [], []
for i in range(len(tiles)):
    for j in range(i, len(tiles)):
        silver.append(rectangle(tiles[i], tiles[j]))
        if check_gold(tiles[i], tiles[j]): 
            gold.append(rectangle(tiles[i], tiles[j]))

print(f"Silver: {max(silver)}\nGold: {max(gold)}")
