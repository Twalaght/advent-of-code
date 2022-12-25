#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

def snafu(num):
	num = num[::-1]

	res = 0
	trans = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
	for i in range(len(num)):
		power = pow(5, i)
		res += trans[num[i]] * power

	return res

def reverse_snafu(num):
	rolling = num
	res = ""

	while rolling > 0:
		tmp = rolling % 5

		if tmp == 3:
			rolling = ((rolling + 2) // 5)
			res += "="
		if tmp == 4:
			rolling = ((rolling + 1) // 5)
			res += "-"
		if tmp == 0:
			rolling = ((rolling - tmp) // 5)
			res += "0"
		if tmp == 1:
			rolling = ((rolling - tmp) // 5)
			res += "1"
		if tmp == 2:
			rolling = ((rolling - tmp) // 5)
			res += "2"

	return res[::-1]

final = 0
for x in data:
	final += snafu(x)

gold = reverse_snafu(final)
print(f"Gold: {gold}")
