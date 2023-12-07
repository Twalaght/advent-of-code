#!/usr/bin/env python3

import functools
import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

backup = data.copy()

def rank(hand: str) -> int:
    counts = sorted([hand.count(x) for x in set(hand)], reverse=True)

    if counts[0] == 5: return 7 # Five of a kind
    if counts[0] == 4: return 6 # Four of a kind
    
    if counts[0] == 3:
        if counts[1] == 2: return 5 # Full house
        return 4 # Three of a kind
    
    if counts[0] == 2:
        if counts[1] == 2: return 3 # Two pair
        return 2 # One pair
    
    return 1

def compare(in_x: str, in_y: str, order: str) -> int:
    x = rank(in_x[0].split()[0])
    y = rank(in_y[0].split()[0])

    if x > y: return 1
    if y > x: return -1

    for x_char, y_char in zip(in_x[1].split()[0], in_y[1].split()[0]):
        if order.index(x_char) < order.index(y_char): return 1
        if order.index(y_char) < order.index(x_char): return -1
    
    return 0

def compare_silver(left: str, right: str) -> int:
    return compare(left, right, "AKQJT98765432")

def compare_gold(left: str, right: str) -> int:
    return compare(left, right, "AKQT98765432J")

def count_winner(data: list, gold: bool):
    res = 0
    for i, hand in enumerate(data, start=1):
        bid = hand[0].split()[-1]
        res += (i * int(bid))
    
    return res

def permute_joker(hand: str) -> list[str]:
    if "J" not in hand: return [hand]

    tmp = []
    for char in "AKQT98765432":
        new = hand.replace("J", char, 1)
        tmp += permute_joker(new)

    return tmp

wild_data = []
for hand in backup:
    tmp = [(x, hand) for x in permute_joker(hand)]
    wild_data.append(sorted(tmp, key=functools.cmp_to_key(compare_gold))[-1])

silver = count_winner(
    sorted([(x, x) for x in data], key=functools.cmp_to_key(compare_silver)),
    False,
)

gold = count_winner(
    sorted(wild_data, key=functools.cmp_to_key(compare_gold)),
    True,
)

print(f"Silver: {silver}\nGold: {gold}")
