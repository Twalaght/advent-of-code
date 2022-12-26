#!/usr/bin/python3

import sys
from copy import deepcopy
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

pos_1 = int(data[0].split()[-1])
pos_2 = int(data[1].split()[-1])
score_1 = 0
score_2 = 0
dice = 1
rolls = 0

def roll_three(dice):
	total = 0

	for i in range(3):
		total += dice
		dice += 1
		if dice > 100: dice = 1

	return dice, total

silver = 0
for i in range(int(1e9)):
	if score_1 >= 1000:
		silver = score_2 * rolls
		break
	if score_2 >= 1000:
		silver = score_1 * rolls
		break

	dice, total = roll_three(dice)
	rolls += 3

	if i % 2 == 0:
		pos_1 += total
		while pos_1 > 10: pos_1 -= 10
		score_1 += pos_1

	else:
		pos_2 += total
		while pos_2 > 10: pos_2 -= 10
		score_2 += pos_2

pos = [int(data[0].split()[-1]), int(data[1].split()[-1])]
score = [0, 0]

def gold(pos, score, game):
	if score[0] >= 21:
		return 1, 0
	if score[1] >= 21:
		return 0, 1

	multi = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]

	total_1 = 0
	total_2 = 0
	player = game % 2

	for x in multi:
		tmp_pos = pos.copy()
		tmp_score = score.copy()

		tmp_pos[player] = tmp_pos[player] + x[0]
		while tmp_pos[player] > 10: tmp_pos[player] -= 10

		tmp_score[player] += tmp_pos[player]

		win_1, win_2 = gold(tmp_pos, tmp_score, game + 1)
		total_1 += (x[1] * win_1)
		total_2 += (x[1] * win_2)

	return total_1, total_2

gold = max(gold(pos, score, 0))

print(f"Silver: {silver}\nGold: {gold}")
