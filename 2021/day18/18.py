#!/usr/bin/python3

import re
import sys
from itertools import permutations as perm
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

def explode(string):
	count = 0
	for i in range(len(string)):
		if string[i] == "[": count += 1
		if string[i] == "]": count -= 1

		if count == 5:
			end_pos = string[i:].find("]") + 1
			target = string[i:i + end_pos]
			string = [string[:i], string[i + end_pos:]]
			break

	if count == 0: return string

	left, right = target[1:-1].split(",")

	l_match = re.findall("\d+", string[0])
	if l_match:
		value = str(int(l_match[-1]) + int(left))
		string[0] = string[0][::-1].replace(l_match[-1][::-1], value[::-1], 1)[::-1]

	r_match = re.findall("\d+", string[1])
	if r_match:
		value = int(r_match[0]) + int(right)
		string[1] = string[1].replace(r_match[0], str(value), 1)

	return f"{string[0]}0{string[1]}"

def split(string):
	match = [x for x in re.findall("\d+", string) if int(x) > 9]
	if not match: return string

	pair = f"[{int(match[0]) // 2},{(int(match[0]) + 1) // 2}]"
	return string.replace(match[0], pair, 1)

def reduce(string):
	if string[0] != "[": return string

	for i in range(len(string)):
		if string[i] == "[": last_left = i
		if string[i] == "]":
			next_right = i + 1
			break

	match = string[last_left : next_right]
	tmp = [int(x) for x in match[1:-1].split(",")]
	value = str(3 * tmp[0] + 2 * tmp[1])
	return string.replace(match, value, 1)

def magnitude(data):
	string = data[0]
	for i in range(1, len(data)):
		string = f"[{string},{data[i]}]"

		while(True):
			exp, spl = explode(string), split(string)

			if exp == spl == string: break

			if exp != string: string = exp
			elif spl != string: string = spl

	while(True):
		new = reduce(string)
		if new == string: break
		string = new

	return int(string)

silver = magnitude(data)
gold = max([magnitude([data[p[0]], data[p[1]]]) for p in perm(range(len(data)), 2)])
print(f"Silver: {silver}\nGold: {gold}")
