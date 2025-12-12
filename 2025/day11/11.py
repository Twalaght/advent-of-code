#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

mapping: dict[str, list[str]] = {}
for row in data:
    left, right = row.split(": ")
    mapping[left] = right.split(" ")

targets = ["fft", "dac"]

def solve(mapping: dict[str, list[str]], start: str) -> dict[int, int]:
    track_map = {k: {0: 0} for k in [*mapping.keys(), "out"]}
    track_map[start][0] = 1

    while True:
        no_move = True
        for k, tracker in track_map.items():
            if not any(tracker.values()):
                continue

            if k == "out":
                continue

            no_move = False

            if k in targets:
                for score in sorted(tracker, reverse=True):
                    if score + 1 < 3:
                        tracker[score + 1] = tracker[score]
                
                tracker[0] = 0

            options = mapping[k]
            for option in options:
                for score, value in tracker.items():
                    track_map[option].setdefault(score, 0)
                    track_map[option][score] += value

            for score in sorted(tracker, reverse=True):
                tracker[score] = 0
        
        if no_move:
            break

    return track_map["out"]

silver, gold = solve(mapping, "you")[0], solve(mapping, "svr")[2]

print(f"Silver: {silver}\nGold: {gold}")
