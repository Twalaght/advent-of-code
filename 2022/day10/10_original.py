#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

data = [[2 if "addx" in x else 1, x] for x in data]

cycle = 1
reg = 1
silver = 0
pixels = [None for _ in range(240)]

while True:
	if (cycle - 1 - 20) % 40 == 0:
		silver += cycle * reg

	if not data: break

	if abs(((cycle - 1) % 40) - reg) < 2:
		pixels[cycle - 1] = "#"
	else:
		pixels[cycle - 1] = "."

	data[0][0] -= 1

	if data[0][0] == 0:
		if "noop" not in data[0]:
			reg += int(data[0][1].split()[-1])

		data.pop(0)

	cycle += 1

print(f"Silver: {silver}\nGold:")
for row in range(6):
	for col in range(40):
		print(pixels[row * 40 + col], end="")
	print()
