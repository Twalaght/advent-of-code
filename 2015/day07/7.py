#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

solves, subs = {}, {}
for line in data:
	inputs, out = line.split(" -> ")
	inputs = inputs.split()

	if len(inputs) == 1: subs[out] = inputs[0]
	if len(inputs) == 2: subs[out] = f"{inputs[1]} {inputs[0]}"
	if len(inputs) == 3: subs[out] = f"{inputs[0]} {inputs[2]} {inputs[1]}"

backup = subs.copy()

def solve(string):
	tmp = string.split()
	if len(tmp) == 1: return int(tmp[0]) if tmp[0].isnumeric() else None

	if len(tmp) == 2:
		if tmp[0].isnumeric():
			tmp = int(tmp[0]) ^ 0xFFFF
			return abs(tmp) - 1 if tmp < 0 else tmp
		else:
			return None

	if len(tmp) == 3:
		if tmp[0].isnumeric() and tmp[1].isnumeric():
			if tmp[2] == "AND": return int(tmp[0]) & int(tmp[1])
			if tmp[2] == "OR": return int(tmp[0]) | int(tmp[1])
			if tmp[2] == "LSHIFT": return int(tmp[0]) << int(tmp[1]) % 65536
			if tmp[2] == "RSHIFT": return int(tmp[0]) >> int(tmp[1])
		else:
			return None

def check():
	remove = []
	for sub in subs:
		string = subs[sub].split()

		for i in range(len(string)):
			if string[i] in solves: string[i] = solves[string[i]]

		res = solve(" ".join(string))
		if res != None:
			solves[sub] = str(res)
			remove.append(sub)

	for i in remove: del subs[i]

while subs: check()
silver = solves["a"]

subs = backup
solves = {}
subs["b"] = silver

while subs: check()
gold = solves["a"]

print(f"Silver: {silver}\nGold: {gold}")
