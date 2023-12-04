#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = [x.split(":")[-1] for x in f.read().splitlines()]

cards = []
for line in data:
    numbers, winners = line.split(" | ")
    numbers = [x for x in numbers.split(" ") if x]
    winners = [x for x in winners.split(" ") if x]

    entry = {
        "numbers": numbers,
        "winners": winners,
    }
    cards.append(entry)

silver = 0
for card in cards:
    n_intersect = len(set(card["winners"]).intersection(set(card["numbers"])))
    if n_intersect:
        silver += pow(2, n_intersect - 1)

n_cards = [1] * len(cards)
for index, card in enumerate(cards):
    for _ in range(n_cards[index]):
        n_intersect = len(set(card["winners"]).intersection(set(card["numbers"])))
        for i in range(n_intersect):
            n_cards[index + 1 + i] += 1

print(f"Silver: {silver}\nGold: {sum(n_cards)}")
