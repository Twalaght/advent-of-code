#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

inv = {"(":")", "[":"]", "{":"}", "<":">"}
score = {")":[3, 1], "]":[57, 2], "}":[1197, 3], ">":[25137, 4]}

silver, gold = 0, []
for line in data:
	stack = []
	for char in line:
		if char in inv:
			stack.append(char)
		elif char != inv[stack.pop()]:
			stack = None
			silver += score[char][0]
			break

	if stack:
		tmp = 0
		for char in reversed(stack): tmp += (tmp * 4) + score[inv[char]][1]
		gold.append(tmp)

gold = sorted(gold)[len(gold) // 2]
print(f"Silver: {silver}\nGold: {gold}")
