#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

silver, gold = 0, 0
for string in data:
	s_flag, g_flag = True, False

	vowels = [[char for char in string].count(vowel) for vowel in ["a", "e", "i", "o", "u"]]
	if sum(vowels) < 3: s_flag = False

	repeat = sum([1 if string[i] == string[i + 1] else 0 for i in range(len(string) - 1)])
	if not repeat: s_flag = False

	if any(naughty in string for naughty in ["ab", "cd", "pq", "xy"]): s_flag = False

	if s_flag: silver += 1

	for i in range(len(string) - 1):
		sample = string[i : i + 2]
		if sample in string[:i] or sample in string[i + 2:]: g_flag = True

	if g_flag and any(string[i] == string[i + 2] for i in range(len(string) - 2)): gold += 1

print(f"Silver: {silver}\nGold: {gold}")
