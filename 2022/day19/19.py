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

# Determine each material is worth 10x the previous one
def heuristic(state):
	return sum([state[3][i] * pow(10, i) for i in range(4)])

def sim(costs, minute_limit, prune):
	states = [(0, (1, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))]
	depth = 0
	max_geodes = 0

	while states:
		mins, robots, mats, mined = states.pop(0)

		# If we enter a new layer, prune before going deeper
		if mins > depth:
			states = sorted(states, key=heuristic)[-prune:]
			depth = mins

		if mins == minute_limit:
			max_geodes = max(max_geodes, mined[3])
			continue

		# Go through a mine cycle, update materials and total mined
		new_mats = tuple([robots[i] + mats[i] for i in range(4)])
		new_mined = tuple([robots[i] + mined[i] for i in range(4)])

		# Add state for if no robot is built
		states.append((mins + 1, robots, new_mats, new_mined))

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

silver, gold = 0, 1
for i in range(len(c_robots)):
	silver += sim(c_robots[i], 24, 200) * (i + 1)
	if i < 3: gold *= sim(c_robots[i], 32, 500)

print(f"Silver: {silver}\nGold: {gold}")
