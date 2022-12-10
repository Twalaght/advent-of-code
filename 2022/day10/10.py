#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

data = [[2] + x.split() if "addx" in x else [1, x] for x in data]

cycle, reg = 0, 1
silver, gold = 0, []

while True:
	if not data: break
	if (cycle - 20) % 40 == 0: silver += (cycle + 1) * reg
	gold.append("#" if abs(cycle % 40 - reg) < 2 else ".")

	data[0][0] -= 1
	if data[0][0] == 0:
		tmp = data.pop(0)
		if tmp[1] == "addx": reg += int(tmp[2])

	cycle += 1

gold = "\n".join(["".join(gold[i * 40: (i + 1) * 40]) for i in range(6)])
print(f"Silver: {silver}\nGold:\n{gold}")
