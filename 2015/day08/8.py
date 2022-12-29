#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

silver, gold = 0, 0
for line in data:
	instr = [char for char in line]

	silver += len(line) + 2
	gold += sum([1 if i == "\"" or i == "\\" else 0 for i in instr]) + 2

	while instr:
		silver -= 1
		if instr.pop(0) == "\\": del instr[:1 if instr[0] in ["\\", "\""] else 3]

print(f"Silver: {silver}\nGold: {gold}")
