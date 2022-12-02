#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
		data = [x.split() for x in f.read().splitlines()]

# Change each move to a 0,1,2 representation
sub = {"A": 0, "X": 0, "B": 1, "Y": 1, "C": 2, "Z": 2}
data = [[sub[x[0]], sub[x[1]]] for x in data]

def play(data, strat):
	tmp = 0
	for game in data:
		# Substitute our move if we're using a strategy
		your_move = (game[0] + game[1] - 1) % 3 if strat else game[1]

		result = (game[0] - your_move) % 3
		if result == 0: tmp += 3 + your_move + 1
		if result == 1: tmp += 0 + your_move + 1
		if result == 2: tmp += 6 + your_move + 1

	return tmp

silver, gold = play(data, False), play(data, True)
print(f"Silver: {silver}\nGold: {gold}")
