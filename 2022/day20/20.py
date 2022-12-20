#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [int(x) for x in f.read().splitlines()]

# Add an index to each value to make them unique
data = [(data[i], i) for i in range(len(data))]

def mix(data, gold):
	if gold: data = [(x[0] * 811589153, x[1]) for x in data]

	for _ in range(10 if gold else 1):
		for i in range(len(data)):
			val = next(x for x in data if x[1] == i)
			idx = data.index(val)
			tmp = data.pop(idx)
			new_idx = (idx + val[0]) % len(data)
			data.insert(new_idx if new_idx else len(data), tmp)

	# Offset the relevant values and calculate the final score
	idx = data.index(next(x for x in data if x[0] == 0))
	return sum([data[(i * 1000 + idx) % len(data)][0] for i in range(1, 4)])

silver, gold = mix(data.copy(), False), mix(data.copy(), True)
print(f"Silver: {silver}\nGold: {gold}")
