#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.split("-") for x in f.read().splitlines()]

silver, gold = 0, 0
for line in data:
	name = "".join(line[:-1])

	counts = []
	for char in set(list(name)):
		counts.append([char, name.count(char)])

	counts.sort(key = lambda x: (-x[1], x[0]))
	true_hash = "".join([x[0] for x in counts])[:5]
	sector, given_hash = line[-1].replace("]", "").split("[")
	
	if true_hash == given_hash: silver += int(sector)

	cipher = lambda c: chr((ord(c) + int(sector) - 97) % 26 + 97)

	real_name = "".join(list(map(cipher, name)))
	if "northpoleobjectstorage" == real_name: gold = sector


print(f"Silver: {silver}\nGold: {gold}")
