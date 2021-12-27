#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

nums = [int(x) for x in data[0].split(",")]
cards = []
for i in range(100):
	cards.append([[int(x) for x in line.split()] for line in data[(i * 6) + 2 : (i * 6) + 7]])

def bingo(card, called):
	lines = [line for line in card] + [[line[i] for line in card] for i in range(5)]

	for line in lines:
		if all(num in called for num in line):
			return sum([sum([x for x in line if x not in called]) for line in card])

	return False

called = []
finished = []
for num in nums:
	called.append(num)

	for card in cards:
		res = bingo(card, called)
		if res:
			finished.append(card)
			if len(cards) == 100: print(f"Silver: {res * num}")
			if len(cards) == 1: print(f"Gold: {res * num}")

	for done in finished: cards.remove(done)
	finished = []
