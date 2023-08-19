#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

data = [x.replace("]", "[").split("[") for x in data]

def tls(segment):
	for i in range(len(segment) - 3):
		if segment[i] == segment[i + 1]: continue

		if segment[i] == segment[i + 3] and segment[i + 1] == segment[i + 2]:
			return True
	
	return False

def ssl(segment):
	groups = []
	for i in range(len(segment) - 2):
		target = (segment[i], segment[i + 1], segment[i + 2])
		if target[0] == target[2]:
			groups.append(target)

	return groups

silver, gold = 0, 0
for line in data:
	abba_outside = False
	abba_inside = False
	for i, segment in enumerate(line):
		
		if i % 2 == 0:
			if tls(segment):
				abba_outside = True

		else:
			if tls(segment):
				abba_inside = True

	if abba_outside and not abba_inside:
		silver += 1

	outsides = []
	insides = []
	for i, segment in enumerate(line):
		if i % 2 == 0:
			tmp = ssl(segment)
			outsides += tmp

		else:
			tmp = ssl(segment)
			insides += tmp
		
	while outsides:
		target = outsides.pop()
		inverse = (target[1], target[0], target[1])

		if inverse in insides:
			gold += 1
			break

print(f"Silver: {silver}\nGold: {gold}")
