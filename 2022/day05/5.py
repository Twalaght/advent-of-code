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

def process_move(stack, moves, gold):
	for move in moves:
		n, fr, to = move[0], move[1] - 1, move[2] - 1
		if gold:
			stack[to] += stack[fr][-n:]
			del stack[fr][-n:]
		else:
			for _ in range(move[0]): stack[to].append(stack[fr].pop())

	return "".join([x[-1] for x in stack])

silver = process_move(*parse_input(data), False)
gold = process_move(*parse_input(data), True)
print(f"Silver: {silver}\nGold: {gold}")

