#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

nums = data[0].split(",")
boards = []
for i in range(100):
	tmp = [i.split() for i in data[(i * 6) + 2 : (i * 6) + 7]]
	for i in range(5):
		for j in range(5):
			tmp[i][j] = {"num": tmp[i][j], "index": 0}

	boards.append(tmp)

def bingo(b_num, c_num):
	rows = [sum(row[i]["index"] for row in boards[b_num]) for i in range(5)]
	cols = [sum(col[i]["index"] for i in range(5)) for col in boards[b_num]]
	sums = rows + cols

	if (5 in sums):
		res = 0
		for i in range(5):
			for j in range(5):
				if boards[b_num][i][j]["index"] == 0:
					res += int(boards[b_num][i][j]["num"])

		return res * int(c_num)

	return 0

test = list(range(100))
for num in nums:
	for b in range(100):
		for i in range(5):
			for j in range(5):
				if (boards[b][i][j]["num"] == num):
					boards[b][i][j]["index"] = 1

		res = bingo(b, num)
		if res != 0:
			if len(test) == 100:
				print(f"Output: {res}")

			if b in test: test.remove(b)
			if not test:
				print(f"Output: {res}")
				exit()
