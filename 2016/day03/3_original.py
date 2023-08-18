#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

h_triangles = [list(map(int, x.split())) for x in data]

v_triangles = []
for i in range(0, len(data), 3):
	group = [list(map(int, x.split())) for x in [data[i], data[i + 1], data[i + 2]]]
	
	for index in range(3):
		tmp = [x[index] for x in group]
		v_triangles.append(tmp)

silver = 0
gold = 0

for triangle in h_triangles:
	triangle.sort()
	if triangle[0] + triangle[1] > triangle[2]:
		silver += 1

for triangle in v_triangles:
	triangle.sort()
	if triangle[0] + triangle[1] > triangle[2]:
		gold += 1

print(f"Silver: {silver}\nGold: {gold}")
