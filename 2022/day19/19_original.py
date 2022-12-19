#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

c_robots = []
for line in data:
	costs = [int(x) for x in line.split(" ") if x.isnumeric()]

	cost_ore = (costs[0], 0, 0, 0)
	cost_clay = (costs[1], 0, 0, 0)
	cost_obs = (costs[2], costs[3], 0, 0)
	cost_geo = (costs[4], 0, costs[5], 0)
	c_robots.append((cost_ore, cost_clay, cost_obs, cost_geo))

def heuristic(state):
	mined = state[3]
	return mined[0] + mined[1] * 10 + mined[2] * 100 + mined[3] * 1000

def sim(costs, minute_limit, prune):
	states = []

	init_minute = 0
	init_robots = (1, 0, 0, 0)
	init_mats = (0, 0, 0, 0)
	init_mined = (0, 0, 0, 0)
	start = (init_minute, init_robots, init_mats, init_mined)

	states.append(start)

	# Aim to BFS
	depth = 0
	max_geodes = 0

	while states:
		mins, robots, mats, mined = states.pop(0)

		# if we enter a new layer, prune
		if mins > depth:
			states = sorted(states, key=heuristic, reverse=True)
			states = states[:prune]
			depth = mins

		if mins == minute_limit:
			max_geodes = max(max_geodes, mined[3])
			continue

		new_mats = tuple([robots[i] + mats[i] for i in range(4)])
		new_mined = tuple([robots[i] + mined[i] for i in range(4)])

		# If we build no robot
		new_state = (mins + 1, robots, new_mats, new_mined)
		states.append(new_state)

		# Try to build each robot
		for robot in range(4):
			# If possible to build the robot
			if all([mats[i] >= costs[robot][i] for i in range(4)]):
				new_robots = list(robots)
				new_robots[robot] += 1
				new_robots = tuple(new_robots)

				# Pay for the robot, update the state, and add it
				paid_mats = tuple([new_mats[i] - costs[robot][i] for i in range(4)])
				new_state = (mins + 1, new_robots, paid_mats, new_mined)
				states.append(new_state)

	return max_geodes

silver = 0
for i in range(len(c_robots)):
	geo = sim(c_robots[i], 24, 1000)
	silver += (geo * (i + 1))

gold = 1
for i in range(3):
	geo = sim(c_robots[i], 32, 10000)
	gold *= geo

print(f"Silver: {silver}\nGold: {gold}")
