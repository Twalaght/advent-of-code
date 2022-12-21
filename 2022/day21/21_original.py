#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

monkeys = {}
for x in data:
	tmp = x.split()
	name = tmp[0][:-1]

	if len(tmp) == 2:
		monkeys[name] = int(tmp[1])
	else:
		monkeys[name] = tmp[1:]

def solve(targ):
	tmp = monkeys[targ]
	if isinstance(tmp, int): return tmp

	left = solve(tmp[0])
	right = solve(tmp[2])

	if tmp[1] == "+": return left + right
	if tmp[1] == "-": return left - right
	if tmp[1] == "*": return left * right
	if tmp[1] == "/": return left / right

silver = int(solve("root"))

def step(humn, left):
	init = solve(monkeys["root"][0]), solve(monkeys["root"][2])
	monkeys["humn"] = humn
	after = solve(monkeys["root"][0]), solve(monkeys["root"][2])

	if left:
		return init[1] - after[0]
	else:
		return init[0] - after[1]

left = True if step(1, True) - step(2, True) != 0 else False

if left:
	lt = True if step(1, True) - step(2, True) < 0 else False
else:
	lt = True if step(1, False) - step(2, False) < 0 else False

rng = [0, int(1e15)]
while True:
	if rng[1] - rng[0] <= 1: break

	avg = ((rng[1] - rng[0]) // 2) + rng[0]
	res = step(avg, left)

	if lt:
		if res < 0:
			rng[0] = avg
		else:
			rng[1] = avg
	else:
		if res > 0:
			rng[0] = avg
		else:
			rng[1] = avg

gold = 0
if step(rng[0], left) == 0: gold = rng[0]
if step(rng[1], left) == 0: gold = rng[1]

print(f"Silver: {silver}\nGold: {gold}")
