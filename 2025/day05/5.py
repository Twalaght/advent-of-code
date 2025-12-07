#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

fresh = [[int(num) for num in x.split("-")] for x in data[:data.index("")]]
ingredients = [int(x) for x in data[data.index("") + 1:]]

silver, gold = 0, 0

timeline = []
for l, r in fresh:
    timeline.append((l, True))
    timeline.append((r + 1, False))

stack = []
clean_timeline = []
for val, start in sorted(list(timeline), key=lambda x: x[0]):
    if start:
        stack.append(val)
    else:
        popped = stack.pop(-1)
        if stack:
            continue

        clean_timeline.append((popped, val))

for target in ingredients:
    for l, r in clean_timeline:
        if l <= target < r:
            silver += 1
            break

for l, r in clean_timeline:
    gold += (r - l)

print(f"Silver: {silver}\nGold: {gold}")
