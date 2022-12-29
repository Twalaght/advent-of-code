#!/usr/bin/python3

import sys
from re import findall
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	string = f.read().strip()

def inc(string):
	chars = [char for char in string]
	for i in range(len(chars) - 1, -1, -1):
		if ord(chars[i]) == 122:
			chars[i] = chr(97)
		else:
			chars[i] = chr(ord(chars[i]) + 1)
			if chars[i] in ["i", "o", "l"]: chars[i] = chr(ord(chars[i]) + 1)
			return "".join(chars)

def check(string):
	if len(set(findall(r"(.)\1", string))) < 2: return False

	chars = [char for char in string]
	for i in range(len(chars) - 2):
		char_1, char_2, char_3 = ord(chars[i]), ord(chars[i + 1]), ord(chars[i + 2])
		if char_1 == char_2 - 1 == char_3 - 2: return True

	return False

while(True):
	string = inc(string)
	res = check(string)
	if res: break

print(f"Silver: {string}")

while(True):
	string = inc(string)
	res = check(string)
	if res: break

print(f"Gold: {string}")
