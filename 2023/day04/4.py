#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = [x.split(":")[-1] for x in f.read().splitlines()]

cards = []
for line in data:
    numbers, winners = line.split(" | ")
    numbers = [x for x in numbers.split(" ") if x]
    winners = [x for x in winners.split(" ") if x]
    cards.append(len(set(winners).intersection(set(numbers))))

silver = 0
n_cards = [1] * len(cards)
for index, card in enumerate(cards):
    if card: silver += pow(2, card - 1)
    for i in range(card): n_cards[index + 1 + i] += n_cards[index]

print(f"Silver: {silver}\nGold: {sum(n_cards)}")
