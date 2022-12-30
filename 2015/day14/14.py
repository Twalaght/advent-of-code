#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x.split() for x in f.read().splitlines()]

reindeer = [(int(x[3]), int(x[6]), int(x[-2])) for x in data]

silver = 0
reindeer_score = [0 for _ in range(len(reindeer))]
for s in range(1, 2503):
	totals = []
	for r in reindeer:
		cycles, offset = divmod(s, (r[1] + r[2]))
		dist = cycles * r[0] * r[1]
		dist += r[0] * min(offset, r[1])
		totals.append(dist)

		silver = max(dist, silver)

	for i in range(len(totals)):
		if totals[i] == max(totals):
			reindeer_score[i] += 1

gold = max(reindeer_score)
print(f"Silver: {silver}\nGold: {gold}")
