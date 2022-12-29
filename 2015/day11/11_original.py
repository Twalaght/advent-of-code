#!/usr/bin/python3

import re
import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	string = f.read().strip()

def inc(string):
	chars = [char for char in string]
	for i in range(len(chars) - 1, -1, -1):
		if ord(chars[i]) == 122:
			chars[i] = chr(97)
		else:
			chars[i] = chr(ord(chars[i]) + 1)
			return "".join(chars)

def check(string):
	chars = [char for char in string]

	flag = False
	for i in range(len(chars) - 2):
		if ord(chars[i]) == ord(chars[i + 1]) - 1:
			if ord(chars[i + 1]) - 1 == ord(chars[i + 2]) - 2:
				flag = True

	if not flag: return False

	for bad in ["i", "o", "l"]:
		if bad in chars: return False

	dubs = set(re.findall(r"(.)\1", "".join(chars)))

	if len(dubs) >= 2:
		return True

	return False

while(True):
	res = check(string)
	if res:
		print(f"Silver: {string}")
		string = inc(string)
		break

	string = inc(string)

while(True):
	res = check(string)
	if res:
		print(f"Gold: {string}")
		break

	string = inc(string)
