#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().strip().split()

row, col = int(data[-3][:-1]), int(data[-1][:-1])

init = 20151125
base = 252533
mod = 33554393

exp = ((row + col - 2) * (row + col - 1) // 2) + col - 1
gold = pow(base, exp, mod) * init % mod

print(f"Gold: {gold}")
