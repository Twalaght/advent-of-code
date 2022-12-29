#!/usr/bin/python3

import sys
from json import loads
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = loads(f.read().strip())

def parse(data, gold):
	tmp = 0
	if type(data) == dict:
		if gold and "red" in data.values(): return 0

		for i in data:
			if type(data[i]) == dict or type(data[i]) == list:
				tmp += parse(data[i], gold)
			elif type(data[i]) == int:
				tmp += data[i]

	if type(data) == list:
		for i in data:
			if type(i) == dict or type(i) == list:
				tmp += parse(i, gold)
			elif type(i) == int:
				tmp += i

	return tmp

silver, gold = parse(data, False), parse(data, True)
print(f"Silver: {silver}\nGold: {gold}")
