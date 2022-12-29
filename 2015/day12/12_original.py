#!/usr/bin/python3

import sys
from json import loads
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = loads(f.read().strip())

def parse(data):
	silver = 0

	if type(data) == dict:
		for i in data:
			if type(data[i]) == dict or type(data[i]) == list:
				silver += parse(data[i])

			elif type(data[i]) == int:
				silver += data[i]

	if type(data) == list:
		for i in data:
			if type(i) == dict or type(i) == list:
				silver += parse(i)
			elif type(i) == int:
				silver += i

	return silver

silver = parse(data)
print(f"Silver: {silver}")

silver = 0

def gold(data):
	silver = 0

	if type(data) == dict:
		if "red" in data.values(): return 0

		for i in data:
			if type(data[i]) == dict or type(data[i]) == list:
				silver += gold(data[i])

			elif type(data[i]) == int:
				silver += data[i]

	if type(data) == list:

		for i in data:
			if type(i) == dict or type(i) == list:
				silver += gold(i)
			elif type(i) == int:
				silver += i

	return silver

gold = gold(data)
print(f"Gold: {gold}")
