#!/usr/bin/env python3

import math
import sys
from typing import NamedTuple
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

class Junction(NamedTuple):
    x: int
    y: int
    z: int

data = [Junction(*[int(x) for x in row.split(",")]) for row in data]

def distance(a: Junction, b: Junction) -> float:
    return math.sqrt(
        ((a.x - b.x) ** 2) +
        ((a.y - b.y) ** 2) +
        ((a.z - b.z) ** 2)
    )

class Span(NamedTuple):
    distance: float
    a:        Junction
    b:        Junction

spans = []
for i in range(len(data)):
    for j in range(i, len(data)):
        a, b = data[i], data[j]
        if a == b:
            continue
        else:
            spans.append(Span(distance(a, b), a, b))

spans = sorted(spans, key=lambda x: x.distance)

circ_to_junc = {i: [data[i]] for i in range(len(data))}

def get_silver(mapping: dict[int, list[Junction]]) -> int:
    silver = 1
    for item in sorted([len(juncs) for juncs in mapping.values()], reverse=True)[:3]:
        silver *= item
    
    return silver

silver = 0
last_connection = None
for join in range(1, int(1e7)):
    if join == 1000:
        silver = get_silver(circ_to_junc)

    if not spans:
        break

    if len(circ_to_junc) == 1:
        break

    span = spans.pop(0)
    
    a_index, b_index = None, None
    for i, juncs in circ_to_junc.items():
        if span.a in juncs:
            a_index = i
        if span.b in juncs:
            b_index = i

    if a_index == b_index:
        continue

    circ_to_junc[a_index].extend(circ_to_junc.pop(b_index))
    last_connection = span

gold = last_connection.a.x * last_connection.b.x

print(f"Silver: {silver}\nGold: {gold}")
