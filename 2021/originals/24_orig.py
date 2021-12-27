#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

blocks = []
for i in range(14):
	tmp = data[i * 18 : (i + 1) * 18]
	blocks.append(tmp)

for i in range(len(blocks)):
	div = blocks[i][4].split()[-1]
	chk = blocks[i][5].split()[-1]
	ofs = blocks[i][15].split()[-1]
	blocks[i] = [div, chk, ofs]
	blocks[i] = [int(char) for char in [div, chk, ofs]]

stack = []
final = []
for i in range(14):
	if blocks[i][1] > 0:
		stack.append([i, blocks[i][2]])
	else:
		tmp = stack.pop()
		ofs = tmp[1] + blocks[i][1]
		final.append([i, tmp[0], ofs])

model = [0] * 14
for eq in final:
	if eq[2] > 0:
		model[eq[0]] = 9
		model[eq[1]] = 9 - eq[2]
	else:
		model[eq[1]] = 9
		model[eq[0]] = 9 + eq[2]

silver = "".join([str(x) for x in model])
print(f"Silver: {silver}")

model = [0] * 14
for eq in final:
	if eq[2] > 0:
		model[eq[1]] = 1
		model[eq[0]] = 1 + eq[2]
	else:
		model[eq[0]] = 1
		model[eq[1]] = 1 - eq[2]

gold = "".join([str(x) for x in model])
print(f"Gold: {gold}")
