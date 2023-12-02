#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

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

def search(line: str, left: bool, gold: bool) -> str:
    for i in range(len(line)):
        tmp = line[i:] if left else line[:len(line) - i]

        if gold:
            for number in mapping:
                if (tmp.startswith if left else tmp.endswith)(number):
                    return str(mapping[number])
        
        if (val := tmp[0 if left else -1]).isnumeric():
            return val

silver, gold = 0, 0
for line in data:
    silver += int(search(line, True, False) + search(line, False, False))
    gold   += int(search(line, True, True)  + search(line, False, True))

print(f"Silver: {silver}\nGold: {gold}")
