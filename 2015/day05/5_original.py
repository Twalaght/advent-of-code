#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

counter = 0
for string in data:
	tmp = 0
	for vowel in ["a", "e", "i", "o", "u"]:
		tmp += [char for char in string].count(vowel)

	if tmp < 3: continue

	tmp = False
	for i in range(len(string) - 1):
		if string[i] == string[i + 1]:
			tmp = True

	if not tmp: continue

	tmp = True
	for naughty in ["ab", "cd", "pq", "xy"]:
		if naughty in string:
			tmp = False

	if not tmp: continue

	counter += 1

print(f"Silver: {counter}")

counter = 0
for string in data:
	flag = False
	for i in range(len(string) - 1):
		tmp = [char for char in string]
		sample = string[i : i + 2]

		left = "".join(tmp[:i])
		right = "".join(tmp[i + 2:])

		if sample in left or sample in right:
			flag = True

	if not flag: continue


	flag = False
	for i in range(len(string) - 2):
		if string[i] == string[i + 2]:
			flag = True

	if not flag: continue

	counter += 1

print(f"Gold: {counter}")
