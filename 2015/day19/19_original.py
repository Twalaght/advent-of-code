#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.split() for x in f.read().splitlines()]

distinct = set()
reps = [(x[0], x[-1]) for x in data[:-2]]
start = data[-1][0]

def replace_nth(sub, repl, original, n):
	tmp = original.split(sub)
	if n + 2 > len(tmp): return None

	left = sub.join(tmp[:n + 1])
	right = sub.join(tmp[n + 1:])

	return left + repl + right

for rep in reps:
	for i in range(len(start)):
		res = replace_nth(rep[0], rep[1], start, i)
		if not res: break
		distinct.add(res)

silver = len(distinct)

# Need to reverse the target for it to work
rev_mol = start[::-1]
undo = {rep[1][::-1]: rep[0][::-1] for rep in reps}

gold = 0
while rev_mol != "e":
	first = [x for x in undo.keys() if x in rev_mol]
	first = sorted(first, key = lambda x: rev_mol.index(x))
	rev_mol = rev_mol.replace(first[0], undo[first[0]], 1)
	gold += 1

print(f"Silver: {silver}\nGold: {gold}")
