#!/usr/bin/python3

import sys
from copy import deepcopy
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()[2:-1]

data = [x[3:].split("#")[:4] for x in data]
rooms = [[{"A": 0, "B": 1, "C": 2, "D": 3}[data[x][room]] for x in [1, 0]] for room in range(4)]
hall = [None] * 11

def permute(state, r_len):
	rooms = deepcopy(state[0])
	hall = deepcopy(state[1])

	states = []
	for r in range(len(rooms)):
		if not any(i != r for i in rooms[r]): continue

		tmp_rooms = deepcopy(rooms)
		mover = tmp_rooms[r].pop()

		for h in [0, 1, 3, 5, 7, 9, 10]:
			room_idx = (r + 1) * 2
			move_max = max(room_idx, h)
			move_min = min(room_idx, h)

			if all(i == None for i in hall[move_min:move_max + 1]):
				tmp = deepcopy(hall)
				tmp[h] = mover
				cost = ((r_len - len(tmp_rooms[r])) + (move_max - move_min)) * (10 ** mover)
				states.append([tmp_rooms, tmp, cost + state[2]])

	if len(states) == 0:
		return None
	else:
		return states

def simple(state, r_len):
	rooms = deepcopy(state[0])
	hall = deepcopy(state[1])

	cost = 0
	flag = True
	while(flag):
		flag = False

		for h in range(len(hall)):
			if hall[h] == None: continue

			room_idx = (hall[h] + 1) * 2
			move_max = max(room_idx, h)
			move_min = min(room_idx, h)

			extra = 1 if room_idx > h else 0

			if all(i == None for i in hall[move_min + extra:move_max + extra]):
				if len(rooms[hall[h]]) < r_len:
					if len(rooms[hall[h]]) == 0 or rooms[hall[h]][0] == hall[h]:
						cost += ((r_len - len(rooms[hall[h]])) + (move_max - move_min)) * (10 ** hall[h])
						rooms[hall[h]].append(hall[h])
						hall[h] = None
						flag = True

	return [rooms, hall, cost + state[2]]

def solved(state, r_len):
	rooms = deepcopy(state[0])
	hall = deepcopy(state[1])

	if not all(i == None for i in hall): return False
	for r in range(len(rooms)):
		if len(rooms[r]) != r_len: return False
		if not all(i == r for i in rooms[r]): return False

	return True

def solve(state, r_len):
	best = int(1e9)

	if (solved(state, r_len)): return state[2]

	opts = permute(state, r_len)
	if opts == None: return best

	for s in range(len(opts)):
		opts[s] = simple(opts[s], r_len)
		tmp = solve(opts[s], r_len)

		if tmp == None:
			continue
		else:
			if tmp < best:
				best = tmp

	return best

silver = solve([deepcopy(rooms), deepcopy(hall), 0], 2)
print(f"Silver: {silver}")

new = [[3, 3], [1, 2], [0, 1], [2, 0]]
for i in range(4):
	rooms[i] = [rooms[i][0]] + new[i] + [rooms[i][1]]

gold = solve([deepcopy(rooms), deepcopy(hall), 0], 4)
print(f"Gold: {gold}")
