#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = [[int(x) for x in line.split()] for line in f.read().splitlines()]

silver = 0
gold = 0
for line in data:
    lines = []
    lines.append(line)

    while True:
        tmp = []
        for i in range(len(lines[-1]) - 1):
            tmp.append(lines[-1][i + 1] - lines[-1][i])
        
        lines.append(tmp)
        if not any(tmp):
            break

    for row in lines:
        silver += row[-1]

    for i, row in enumerate(lines):
        if i % 2 == 0:
            gold += row[0]
        else:
            gold -= row[0]
    
print(f"Silver: {silver}\nGold: {gold}")
