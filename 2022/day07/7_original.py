#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.split() for x in f.read().splitlines()]

from functools import reduce
from operator import getitem

def get_fs(fs, idx_list): return reduce(getitem, idx_list, fs)
def set_fs(fs, idx_list, value): get_fs(fs, idx_list[:-1])[idx_list[-1]] = value

fs = {"/": {}}
pwd = []
for cmd in data:
	# Handle directory changes
	if cmd[0] == "$":
		if cmd[1] == "cd":
			if cmd[-1] == "..":
				pwd.pop()
			else:
				pwd.append(cmd[-1])

	# If not a dir change, it's ls output
	else:
		tmp_pwd = pwd + [cmd[1]]
		if cmd[0] == "dir":
			set_fs(fs, tmp_pwd, {})
		else:
			set_fs(fs, tmp_pwd, int(cmd[0]))

def solve(fs):
	folders = []

	for i in fs:
		if type(fs[i]) == dict:
			fs[i], tmp = solve(fs[i])
			folders += tmp

	total = 0
	for i in fs:
		total += fs[i]

	folders += [total]
	return total, folders

fs, folders = solve(fs)

silver = sum([x for x in folders if x < 100000])

req_free = 30000000 - (70000000 - fs)
gold = min([x for x in folders if x > req_free])

print(f"Silver: {silver}\nGold: {gold}")
