#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.replace(",", "").split() for x in f.read().splitlines()]

def sim(a, b):
	ctr = 0
	while True:
		if ctr >= len(data): break
		ins = data[ctr]

		if ins[0] == "hlf":
			if ins[1] == "a": a //= 2
			if ins[1] == "b": b //= 2

		if ins[0] == "tpl":
			if ins[1] == "a": a *= 3
			if ins[1] == "b": b *= 3

		if ins[0] == "inc":
			if ins[1] == "a": a += 1
			if ins[1] == "b": b += 1

		if ins[0] == "jmp":
			ctr += int(ins[1])
			continue

		if ins[0] == "jie":
			if ins[1] == "a" and a % 2 == 0:
				ctr += int(ins[2])
				continue
			if ins[1] == "b" and b % 2 == 0:
				ctr += int(ins[2])
				continue

		if ins[0] == "jio":
			if ins[1] == "a" and a == 1:
				ctr += int(ins[2])
				continue
			if ins[1] == "b" and b == 1:
				ctr += int(ins[2])
				continue

		ctr += 1

	return b

silver, gold = sim(0, 0), sim(1, 0)
print(f"Silver: {silver}\nGold: {gold}")
