#!/usr/bin/python3

import copy
import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

monkeys = []
for i in range(len(data) // 7 + 1):
	tmp = data[i * 7: i * 7 + 6]

	items = [int(x) for x in tmp[1].split(": ")[-1].split(", ")]

	op = tmp[2].split("new = old ")[-1].split()

	test = int(tmp[3].split()[-1])

	res = [int(tmp[x].split()[-1]) for x in [4, 5]]

	monkey = {"items": items, "op": op, "test": test, "res": res}
	monkeys.append(monkey)

def perform_op(old, op):
	res = old
	if op[1] == "old":
		if op[0] == "*":
			res *= res
		else:
			res += res

	else:
		if op[0] == "*":
			res *= int(op[1])
		else:
			res += int(op[1])

	return res

def simulate(monkeys, rounds, lcd):
	inspect = [0 for _ in range(len(monkeys))]

	for _ in range(rounds):
		for i in range(len(monkeys)):
			while monkeys[i]["items"]:
				inspect[i] += 1
				tmp = monkeys[i]["items"].pop(0)
				tmp = perform_op(tmp, monkeys[i]["op"])

				if lcd:
					tmp %= lcd
				else:
					tmp //= 3

				if tmp % monkeys[i]["test"] == 0:
					target = monkeys[i]["res"][0]
				else:
					target = monkeys[i]["res"][1]

				monkeys[target]["items"].append(tmp)

	return inspect

inspect = simulate(copy.deepcopy(monkeys), 20, None)
silver = sorted(inspect)
silver = silver[-1] * silver[-2]

tmp = [x["test"] for x in monkeys]
lcd = 1
for x in tmp: lcd *= x

inspect = simulate(copy.deepcopy(monkeys), 10000, lcd)
gold = sorted(inspect)
gold = gold[-1] * gold[-2]

print(f"Silver: {silver}\nGold: {gold}")
