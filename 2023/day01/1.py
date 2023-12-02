#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

numeric_only_data = ["".join([c for c in line if c.isnumeric()]) for line in data]

silver = 0
for line in numeric_only_data:
    silver += int(line[0] + line[-1])

mapping = {
    "one":   "1",
    "two":   "2",
    "three": "3",
    "four":  "4",
    "five":  "5",
    "six":   "6",
    "seven": "7",
    "eight": "8",
    "nine":  "9",
}

def find_left(line) -> int:
    for i in range(len(line)):
        tmp = line[i:]
        for number in mapping:
            if tmp.startswith(number):
                return mapping[number]
        
        if tmp[0].isnumeric():
            return tmp[0]
        
def find_right(line) -> int:
    for i in range(len(line)):
        tmp = line[:len(line) - i]
        for number in mapping:
            if tmp.endswith(number):
                return mapping[number]
        
        if tmp[-1].isnumeric():
            return tmp[-1]

gold = 0
for line in data:
    gold += int(find_left(line) + find_right(line))

print(f"Silver: {silver}\nGold: {gold}")
