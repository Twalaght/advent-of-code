#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

mem = 0
lit = 0
for line in data:
	fixed = []
	instr = [char for char in line]

	while instr:
		char = instr.pop(0)

		if char != "\\":
			fixed.append(char)
			continue

		char = instr.pop(0)

		if char == "\\" or char == "\"":
			fixed.append(char)
			continue

		d_1 = instr.pop(0)
		d_2 = instr.pop(0)

		tmp = f"{d_1}{d_2}"
		fixed.append(chr(int(tmp, 16)))

	fixed = "".join(fixed)

	mem += len(line)
	lit += len(fixed) - 2

print(f"Silver: {mem - lit}")

mem = 0
lit = 0
for line in data:
	fixed = []
	instr = [char for char in line]

	fixed.append("\"")
	for i in instr:
		if i == "\"":
			fixed.append("\\")
			fixed.append("\"")
			continue

		if i == "\\":
			fixed.append("\\\\")
			continue

		fixed.append(i)

	fixed.append("\"")

	fixed = "".join(fixed)

	mem += len(line)
	lit += len(fixed)

print(f"Gold: {lit - mem}")
