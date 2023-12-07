#!/usr/bin/env python3

import functools
import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

backup = data.copy()

def rank(hand: str) -> int:
    hand = [char for char in hand]

    counts = sorted([hand.count(x) for x in set(hand)], reverse=True)

    # Five of a kind
    if counts[0] == 5:
        return 7

    # Four of a kind
    if counts[0] == 4:
        return 6
    
    # Full house
    if counts[0] == 3 and counts[1] == 2:
        return 5
    
    # Three of a kind
    if counts[0] == 3:
        return 4

    # Two pair
    if counts[0] == 2 and counts[1] == 2:
        return 3

    # One pair
    if counts[0] == 2:
        return 2
    
    return 1

def compare(x: str, y: str) -> int:
    x = x.split()[0]
    y = y.split()[0]

    x_1 = rank(x)
    y_1 = rank(y)

    if x_1 > y_1: return 1
    if y_1 > x_1: return -1

    valid = "AKQJT98765432"
    for i, (x_char, y_char) in enumerate(zip(x, y)):
        if valid.index(x_char) < valid.index(y_char): return 1
        if valid.index(y_char) < valid.index(x_char): return -1
    
    return 0

data.sort(key=functools.cmp_to_key(compare))

silver = 0
for i, hand in enumerate(data, start=1):
    bid = hand.split()[-1]
    silver += (i * int(bid))

def permute_joker(hand: str) -> list[str]:
    valid = "AKQT98765432"

    if "J" not in hand: return [hand]

    tmp = []
    for char in valid:
        new = hand.replace("J", char, 1)
        tmp += permute_joker(new)

    return tmp

def compare_two(in_x: str, in_y: str) -> int:
    x = in_x[0].split()[0]
    y = in_y[0].split()[0]

    x_1 = rank(x)
    y_1 = rank(y)

    if x_1 > y_1: return 1
    if y_1 > x_1: return -1

    valid = "AKQT98765432J"
    for i, (x_char, y_char) in enumerate(zip(in_x[1].split()[0], in_y[1].split()[0])):
        if valid.index(x_char) < valid.index(y_char): return 1
        if valid.index(y_char) < valid.index(x_char): return -1

data = []
for hand in backup:
    if "J" not in hand:
        data.append((hand, hand))
        continue

    tmp = permute_joker(hand)
    tmp.sort(key=functools.cmp_to_key(compare))
    data.append((tmp[-1], hand))

data.sort(key=functools.cmp_to_key(compare_two))

gold = 0
for i, hand in enumerate(data, start=1):
    bid = hand[0].split()[-1]
    gold += (i * int(bid))

print(f"Silver: {silver}\nGold: {gold}")
