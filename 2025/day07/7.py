#!/usr/bin/env python3

import sys
from functools import lru_cache
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = [list(x) for x in f.read().splitlines()]

silver = set()

@lru_cache(maxsize=None)
def search(y: int, x: int) -> int:
    new_y = y + 1
    if new_y == len(data):
        return 1
    elif data[new_y][x] == "^":
        silver.add((new_y, x))
        return search(new_y, x - 1) + search(new_y, x + 1)
    
    return search(new_y, x)

gold = search(0, data[0].index("S"))

print(f"Silver: {len(silver)}\nGold: {gold}")
