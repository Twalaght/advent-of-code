#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [int(x) for x in f.read().splitlines()]

data = [(data[i], i) for i in range(len(data))]

def mix(n, data):
	for _ in range(n):
		for i in range(len(data)):
			val = [x for x in data if x[1] == i][0]
			idx = data.index(val)

			tmp = data.pop(idx)
			new_idx = (idx + val[0]) % len(data)
			if new_idx == 0: new_idx = len(data)

			data.insert(new_idx, tmp)

	return data

backup = data.copy()

data = mix(1, data)
tmp = [x for x in data if x[0] == 0][0]
idx = data.index(tmp)

silver = 0
for i in range(1, 4):
	silver += data[(i * 1000 + idx) % len(data)][0]

data = backup
data = [(x[0] * 811589153, x[1]) for x in data]
data = mix(10, data)
tmp = [x for x in data if x[0] == 0][0]
idx = data.index(tmp)

gold = 0
for i in range(1, 4):
	gold += data[(i * 1000 + idx) % len(data)][0]

print(f"Silver: {silver}\nGold: {gold}")
