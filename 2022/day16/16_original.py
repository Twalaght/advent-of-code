#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

flows = {}
tuns = {}
for line in data:
	tmp = line.replace(",","").split(" ")
	v = tmp[1]
	flow = tmp[4][5:-1]

	flows[v] = int(flow)
	tuns[v] = tmp[9:]

mem, opened = {}, []

def silver(t, pos, ticks, mem, opened):
	# Return early if we've seen this node, at this time, with a better score
	if mem.get((t, pos), -1) >= sum(ticks): return -1
	mem[(t, pos)] = sum(ticks)

	# If time is reached, return the flow score
	if t == 30: return sum(ticks)

	# If current can be opened, and it's not a zero flow
	scores = []
	if pos not in opened and flows[pos] > 0:
		opened.append(pos)
		tick = sum(flows[x] for x in opened)
		score = silver(t + 1, pos, ticks + [tick], mem, opened)
		scores.append(score)
		opened.remove(pos)

	# Simulate every other move we can make
	tick = sum(flows[x] for x in opened)
	for move in tuns[pos]:
		score = silver(t + 1, move, ticks + [tick], mem, opened)
		scores.append(score)

	return max(scores)

mem, opened = {}, []

def gold(t, pos_1, pos_2, ticks, mem, opened):
	# Return early if we've seen this node, at this time, with a better score
	if mem.get((t, pos_1, pos_2), -1) >= sum(ticks): return -1
	mem[(t, pos_1, pos_2)] = sum(ticks)

	# If time is reached, return the flow score
	if t == 26: return sum(ticks)

	# all open?
	if len(opened) == len([x for x in flows if flows[x] != 0]):
		tick = sum(flows[x] for x in opened)
		return gold(t + 1, pos_1, pos_2, ticks + [tick], mem, opened)

	scores = []
	if pos_1 not in opened and flows[pos_1] > 0:
		opened.append(pos_1)

		# Elephant loop
		if pos_2 not in opened and flows[pos_2] > 0:
			opened.append(pos_2)
			tick = sum(flows[x] for x in opened)
			score = gold(t + 1, pos_1, pos_2, ticks + [tick], mem, opened)
			scores.append(score)
			opened.remove(pos_2)

		tick = sum(flows[x] for x in opened)
		for move in tuns[pos_2]:
			score = gold(t + 1, pos_1, move, ticks + [tick], mem, opened)
			scores.append(score)

		opened.remove(pos_1)

	# Simulate every other move we can make
	tick = sum(flows[x] for x in opened)
	for move in tuns[pos_1]:

		# Elephant loop
		if pos_2 not in opened and flows[pos_2] > 0:
			opened.append(pos_2)
			tick = sum(flows[x] for x in opened)
			score = gold(t + 1, move, pos_2, ticks + [tick], mem, opened)
			scores.append(score)
			opened.remove(pos_2)

		tick = sum(flows[x] for x in opened)
		for move_2 in tuns[pos_2]:
			score = gold(t + 1, move, move_2, ticks + [tick], mem, opened)
			scores.append(score)

	return max(scores)


silver = silver(1, "AA", [0], mem, opened)
gold = gold(1, "AA", "AA", [0], mem, opened)
print(f"Silver: {silver}\nGold: {gold}")
