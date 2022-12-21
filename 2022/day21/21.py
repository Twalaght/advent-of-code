#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

monkeys = {}
for x in data:
	tmp = x.split()
	monkeys[tmp[0][:-1]] = int(tmp[1]) if len(tmp) == 2 else tmp[1:]

def solve(target):
	tmp = monkeys[target]
	if isinstance(tmp, int): return tmp

	left, right = solve(tmp[0]), solve(tmp[2])

	if tmp[1] == "+": return left + right
	if tmp[1] == "-": return left - right
	if tmp[1] == "*": return left * right
	if tmp[1] == "/": return left / right

init = solve(monkeys["root"][0]), solve(monkeys["root"][2])

def step(humn, left):
	monkeys["humn"] = humn
	after = solve(monkeys["root"][0]), solve(monkeys["root"][2])
	return init[1] - after[0] if left else init[0] - after[1]

silver = int(solve("root"))

# Determine the side to look at, and the comparison operator
left = True if step(1, True) - step(2, True) != 0 else False
lt = True if step(1, left) - step(2, left) < 0 else False

# Binary search for the "humn" value
rng = [0, int(1e15)]
while rng[1] - rng[0] > 1:
	avg = ((rng[1] - rng[0]) // 2) + rng[0]
	res = step(avg, left)
	rng[0 if (lt and res < 0) or (not lt and res > 0) else 1] = avg

gold = int([x for x in rng if step(x, left) == 0][0])

print(f"Silver: {silver}\nGold: {gold}")
