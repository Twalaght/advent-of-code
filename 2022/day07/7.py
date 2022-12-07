#!/usr/bin/python3

import sys
from functools import reduce
from operator import getitem
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.split() for x in f.read().splitlines()]

# Set value of an item in nested dictionary with a list as the index
def set_fs(fs, idx_list, value): reduce(getitem, idx_list[:-1], fs)[idx_list[-1]] = value

fs, pwd = {"/": {}}, []
for cmd in data:
	# Handle ls output
	if cmd[0] != "$":
		val = {} if cmd[0] == "dir" else int(cmd[0])
		set_fs(fs, pwd + [cmd[1]], val)

	# Handle directory changes
	elif cmd[1] == "cd":
		pwd.pop() if cmd[2] == ".." else pwd.append(cmd[2])

# Find each folder size recursively
def solve(fs):
	folders = []
	for i in fs:
		if type(fs[i]) == dict:
			fs[i], tmp = solve(fs[i])
			folders += tmp

	total = sum([fs[i] for i in fs])
	return total, folders + [total]

total, folders = solve(fs)
silver = sum([x for x in folders if x < 100000])
gold = min([x for x in folders if x > (3e7 - (7e7 - total))])
print(f"Silver: {silver}\nGold: {gold}")
