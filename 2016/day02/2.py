#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

silver, gold = "", ""
gold_pad = [
	[0,  0,  1,  0, 0],
	[0,  2,  3,  4, 0],
	[5,  6,  7,  8, 9],
	[0, 10, 11, 12, 0],
	[0,  0, 13,  0, 0]
]

def move_key(pos: list, mod: tuple, gold: bool):
	new_pos = [pos[0] + mod[0], pos[1] + mod[1]]

	for index in new_pos:
		if index >= (5 if gold else 3) or index < 0: return pos
	
	if gold and gold_pad[new_pos[0]][new_pos[1]] == 0: return pos

	return new_pos

mod = {
	"U": (-1, 0),
	"D": (1, 0),
	"L": (0, -1),
	"R": (0, 1)
}
silver_pos, gold_pos = [1, 1], [2, 0]

for moves in data:
	for move in moves:
		silver_pos = move_key(silver_pos, mod[move], False)
		gold_pos = move_key(gold_pos, mod[move], True)

	silver += str((silver_pos[0] * 3) + silver_pos[1] + 1)
	gold += hex(gold_pad[gold_pos[0]][gold_pos[1]])[2:].upper()

print(f"Silver: {silver}\nGold: {gold}")
