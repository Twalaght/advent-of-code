#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

blocks = []
for i in range(14):
	tmp = data[i * 18 : (i + 1) * 18]
	blocks.append([int(tmp[x].split()[-1]) for x in [4, 5, 15]])

stack = []
for i in range(14):
	if blocks[i][1] > 0:
		stack.append([i, blocks[i][2]])
	else:
		tmp = stack.pop()
		stack.insert(0, [i, tmp[0], tmp[1] + blocks[i][1]])

silver, gold = [0] * 14, [0] * 14
for eq in stack:
	bit = int(eq[2] > 0)

	silver[eq[(bit + 1) % 2]] = 9
	silver[eq[bit]] = 9 + (eq[2] if not bit else -eq[2])

	gold[eq[bit]] = 1
	gold[eq[(bit + 1) % 2]] = 1 + (eq[2] if bit else -eq[2])

silver = "".join([str(x) for x in silver])
gold = "".join([str(x) for x in gold])
print(f"Silver: {silver}\nGold: {gold}")
