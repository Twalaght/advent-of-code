#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [[int(char) for char in x] for x in f.read().splitlines()]

copy = data

len = 10
silver = 0

def flash(x, y):
	if x != 0:
		if y != 0:
			data[x - 1][y - 1] += 1
		if y != len - 1:
			data[x - 1][y + 1] += 1

		data[x - 1][y] += 1

	if x != len - 1:
		if y != 0:
			data[x + 1][y - 1] += 1
		if y != len - 1:
			data[x + 1][y + 1] += 1

		data[x + 1][y] += 1

	if y != 0:
		data[x][y - 1] += 1
	if y != len - 1:
		data[x][y + 1] += 1

	data[x][y] = -99

for step in range(100):

	# Increment
	for i in range(len):
		for j in range(len):
			data[i][j] += 1

	# Flash
	while (True):
		okay = True

		for i in range(len):
			for j in range(len):
				if data[i][j] > 9:
					flash(i, j)
					silver += 1
					okay = False

		if okay:
			break

	for i in range(len):
		for j in range(len):
			if data[i][j] < 0:
				data[i][j] = 0

print(f"Silver: {silver}")

data = copy

for step in range(int(1e9)):
	# Increment
	for i in range(len):
		for j in range(len):
			data[i][j] += 1

	# Flash
	while (True):
		okay = True

		for i in range(len):
			for j in range(len):
				if data[i][j] > 9:
					flash(i, j)
					silver += 1
					okay = False

		if okay:
			break

	for i in range(len):
		for j in range(len):
			if data[i][j] < 0:
				data[i][j] = 0

	gold = True
	for i in range(len):
		for j in range(len):
			if data[i][j] > 0:
				gold = False

	if gold:
		print(f"Gold: {step + 1}")
		exit()
