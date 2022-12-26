#!/usr/bin/python3

import math
import re
import sys
from itertools import permutations
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

def explode(string):
	target = ""
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

	l_match = re.findall("[0-9]+", string[0])
	if l_match:
		backmatch = l_match[-1][::-1]
		value = str(int(l_match[-1]) + int(left))

		string[0] = string[0][::-1]
		string[0] = string[0].replace(backmatch, value[::-1], 1)
		string[0] = string[0][::-1]

	r_match = re.findall("[0-9]+", string[1])
	if r_match:
		value = int(r_match[0]) + int(right)
		string[1] = string[1].replace(r_match[0], str(value), 1)

	return f"{string[0]}0{string[1]}"

def split(string):
	match = [x for x in re.findall("[0-9]+", string) if int(x) > 9]

	if not match: return string

	tmp = int(match[0]) / 2
	left = math.floor(tmp)
	right = math.ceil(tmp)

	new = f"[{left},{right}]"

	string = string.replace(match[0], new, 1)
	return string

def reduce(string):
	if string[0] != "[": return string

	last_left = -1
	next_right = -1
	for i in range(len(string)):
		if string[i] == "[": last_left = i
		if string[i] == "]":
			next_right = i + 1
			break

	tmp = string[last_left : next_right]
	match = tmp
	tmp = [int(x) for x in tmp[1:-1].split(",")]
	tmp = str(3 * tmp[0] + 2 * tmp[1])

	string = string.replace(match, tmp, 1)
	return string

def magnitude(data):
	string = data[0]
	for i in range(1, len(data)):
		string = f"[{string},{data[i]}]"
		while(True):
			new = explode(string)

			if new != None and new != string:
				string = new
				continue

			new = split(string)
			if new != None and new != string:
				string = new
				continue

			break

	while(True):
		new = reduce(string)

		if new != string:
			string = new
			continue

		break

	return int(string)

silver = magnitude(data)
print(f"Silver: {silver}")

perm = permutations(range(len(data)), 2)
gold = 0
for p in perm:
	pair = [data[p[0]], data[p[1]]]

	tmp = magnitude(pair)
	if tmp > gold: gold = tmp

print(f"Gold: {gold}")
