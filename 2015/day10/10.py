#!/usr/bin/python3

import sys
from re import sub
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	string = f.read().strip()

def replace(match):
	string = match.group(1)
	return str(len(string)) + string[0]

for i in range(1, 51):
	string = sub(r"((\d)\2*)", replace, string)
	if i == 40: print(f"Silver: {len(string)}")
	if i == 50: print(f"Gold: {len(string)}")
