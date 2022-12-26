#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

inv = {"(":")", "[":"]", "{":"}", "<":">"}
pairs = {")":"(", "]":"[", "}":"{", ">":"<"}

score = {")":3, "]":57, "}":1197, ">":25137}
syntax = 0

gold_score = {")":1, "]":2, "}":3, ">":4}
gold = []

for i in range(len(data)):
	stack = []
	valid = True
	for char in data[i]:
		if char in pairs.values():
			stack.append(char)
		else:
			stk_chr = stack.pop()
			if char != inv[stk_chr]:
				valid = False
				syntax += score[char]
				break

	if len(stack) != 0:
		if valid:
			stack.reverse()

			tmp = 0
			for char in stack:
				tmp *= 5
				tmp += gold_score[inv[char]]

			gold.append(tmp)

print(f"Silver: {syntax}")
gold = sorted(gold)
print(f"Gold: {gold[len(gold) // 2]}")
