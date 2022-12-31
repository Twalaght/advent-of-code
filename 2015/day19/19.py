#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.split() for x in f.read().splitlines()]

# Need to reverse the target for it to work, so reverse subs too
reps = [(x[0][::-1], x[-1][::-1]) for x in data[:-2]]
undo = {rep[1]: rep[0] for rep in reps}
start = data[-1][0][::-1]
distinct = set()

def replace_nth(sub, repl, original, n):
	tmp = original.split(sub)
	if n + 2 > len(tmp): return None
	return sub.join(tmp[:n + 1]) + repl + sub.join(tmp[n + 1:])

for rep in reps:
	for i in range(len(start)):
		res = replace_nth(rep[0], rep[1], start, i)
		if not res: break
		distinct.add(res)

silver = len(distinct)

gold = 0
while start != "e":
	first = [x for x in undo.keys() if x in start]
	first = sorted(first, key = lambda x: start.index(x))
	start = start.replace(first[0], undo[first[0]], 1)
	gold += 1

print(f"Silver: {silver}\nGold: {gold}")
