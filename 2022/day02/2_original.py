#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
		data = [x.split() for x in f.read().splitlines()]

silver, gold = 0, 0
shape_score = {"X": 1, "Y": 2, "Z": 3}
shape_score_op = {"A": 1, "B": 2, "C": 3}

def game_score(opponent, you):
	if opponent == "A":
		if you == "X": return 3

		if you == "Y":
			return 6
		elif you == "Z":
			return 0

	if opponent == "B":
		if you == "Y": return 3

		if you == "X":
			return 0
		elif you == "Z":
			return 6

	if opponent == "C":
		if you == "Z": return 3

		if you == "X":
			return 6
		elif you == "Y":
			return 0

for game in data:
	silver += game_score(game[0], game[1])
	silver += shape_score[game[1]]

for game in data:
	if game[1] == "X":
		gold += 0

		if game[0] == 'A':
			gold += 3
		elif game[0] == 'B':
			gold += 1
		else:
			gold += 2

	if game[1] == "Y":
		gold += shape_score_op[game[0]]
		gold += 3

	if game[1] == "Z":
		gold += 6
		if game[0] == 'A':
			gold += 2
		elif game[0] == 'B':
			gold += 3
		else:
			gold += 1

print(f"Silver: {silver}\nGold: {gold}")
