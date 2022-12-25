#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

def snafu(n):
	trans = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
	return sum([trans[n[::-1][i]] * pow(5, i) for i in range(len(n))])

def reverse_snafu(n):
	res = ""
	while n > 0:
		trans = {0: [0, "0"], 1: [1, "1"], 2: [2, "2"], 3: [-2, "="], 4: [-1, "-"]}
		res += trans[n % 5][1]
		n = (n - trans[n % 5][0]) // 5

	return res[::-1]

gold = reverse_snafu(sum([snafu(x) for x in data]))
print(f"Gold: {gold}")
