#!/usr/bin/python3

import copy
import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

monkeys = []
for i in range(len(data) // 7 + 1):
	items = [int(x) for x in data[i * 7 + 1].split(": ")[-1].split(", ")]
	tmp = [x.split() for x in data[i * 7 + 2: i * 7 + 6]]
	monkeys.append({"items": items,
					"op": tmp[0][-2:],
					"test": int(tmp[1][-1]),
					"res": [int(tmp[x][-1]) for x in [2, 3]]})

def perform_op(old, op):
	val = old if op[1] == "old" else int(op[1])
	return old * val if op[0] == "*" else old + val

def simulate(monkeys, rounds, lcd):
	inspect = [0 for _ in range(len(monkeys))]
	for _ in range(rounds):
		for i in range(len(monkeys)):
			while monkeys[i]["items"]:
				# Inspect the item
				inspect[i] += 1
				item = monkeys[i]["items"].pop(0)
				item = perform_op(item, monkeys[i]["op"])
				item = item % lcd if lcd else item // 3

				# Throw the item
				target = 0 if item % monkeys[i]["test"] == 0 else 1
				target = monkeys[i]["res"][target]
				monkeys[target]["items"].append(item)

	inspect = sorted(inspect)
	return inspect[-1] * inspect[-2]

lcm = 1
for x in [x["test"] for x in monkeys]: lcm *= x

silver = simulate(copy.deepcopy(monkeys), 20, None)
gold = simulate(copy.deepcopy(monkeys), 10000, lcm)
print(f"Silver: {silver}\nGold: {gold}")
