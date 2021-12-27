#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

pos = [int(data[0].split()[-1]) - 1, int(data[1].split()[-1]) - 1]
score = [0, 0]

def silver(pos, score):
	for i in range(1000):
		if max(score) >= 1000: return min(score) * i * 3

		rolls = ((i * 3 * 3) + 6) % 10
		pos[i % 2] = (pos[i % 2] + rolls) % 10
		score[i % 2] += pos[i % 2] + 1

mem = {}
def gold(pos, score, game):
	if max(score) >= 21: return [1, 0] if score[0] >= 21 else [0, 1]

	total = [0, 0]
	player = game % 2

	for uni in [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]:
		tmp_pos, tmp_score = pos.copy(), score.copy()

		tmp_pos[player] = (tmp_pos[player] + uni[0]) % 10
		tmp_score[player] += tmp_pos[player] + 1

		key = (tmp_pos[0], tmp_pos[1], tmp_score[0], tmp_score[1], game % 2)
		if key not in mem: mem[key] = gold(tmp_pos, tmp_score, game + 1)

		total = [total[0] + (uni[1] * mem[key][0]), total[1] + (uni[1] * mem[key][1])]

	return total

silver = silver(pos.copy(), score.copy())
gold = gold(pos.copy(), score.copy(), 0)
print(f"Silver: {silver}\nGold: {max(gold)}")
