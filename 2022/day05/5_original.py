#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

def parse_input(data):
	breaker = data.index("")

	# Make blank lists for each crane column
	size = len(data[breaker - 1].split())
	stack = [[] for _ in range(size)]

	# Process existing crates
	crane = data[:breaker - 1][::-1]
	for row in crane:
		for i in range(size):
			char = row[1 + (i * 4)]

			if char != " ": stack[i].append(char)

	# Process the move list
	moves = data[breaker + 1:]
	moves = [[int(n) for n in x.split() if n.isnumeric()] for x in moves]
	return stack, moves

silver, gold = "", ""

stack, moves = parse_input(data)
for move in moves:
	for _ in range(move[0]):
		tmp = stack[move[1] - 1].pop()
		stack[move[2] - 1].append(tmp)

for x in stack: silver += x[-1]


stack, moves = parse_input(data)
for move in moves:
	tmp = stack[move[1] - 1][-move[0]:]
	stack[move[2] - 1] += tmp
	del stack[move[1] - 1][-move[0]:]

for x in stack: gold += x[-1]

print(f"Silver: {silver}\nGold: {gold}")
