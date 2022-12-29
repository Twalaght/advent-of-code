#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

solves = {}
subs = {}

for i in data:
	inputs, out = i.split(" -> ")
	inputs = inputs.split()

	final = ""
	if len(inputs) == 1: final = inputs[0]
	if len(inputs) == 2: final = f"{inputs[1]} {inputs[0]}"
	if len(inputs) == 3: final = f"{inputs[0]} {inputs[2]} {inputs[1]}"
	subs[out] = final

backup = subs.copy()

def solve(string):
	tmp = string.split()

	if len(tmp) == 1:
		if tmp[0].isnumeric():
			return int(tmp[0])
		else:
			return None

	if len(tmp) == 2:
		if tmp[0].isnumeric():
			test = int(tmp[0]) ^ 0xFFFF
			if test < 0: test = abs(test) - 1
			return test
		else:
			return None

	if len(tmp) == 3:
		if tmp[0].isnumeric() and tmp[1].isnumeric():
			if tmp[2] == "AND": return int(tmp[0]) & int(tmp[1])
			if tmp[2] == "OR": return int(tmp[0]) | int(tmp[1])
			if tmp[2] == "LSHIFT": return (int(tmp[0]) << int(tmp[1])) % 65536
			if tmp[2] == "RSHIFT": return (int(tmp[0]) >> int(tmp[1]))
		else:
			return None

def check():
	add = []
	remove = []

	for sub in subs:
		string = subs[sub].split()

		for i in range(len(string)):
			if string[i] in solves:
				string[i] = solves[string[i]]

		string = " ".join(string)

		res = solve(string)
		if res != None:
			add.append([sub, str(res)])
			remove.append(sub)

	for i in add:
		solves[i[0]] = i[1]
	for i in remove:
		del subs[i]

while subs: check()

silver = solves["a"]
print(f"Silver: {silver}")

subs = backup
solves = {}
subs["b"] = silver

while subs: check()

gold = solves["a"]
print(f"Gold: {gold}")
