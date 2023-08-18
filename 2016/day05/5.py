#!/usr/bin/python3

import hashlib
import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().strip()

md5 = lambda string: hashlib.md5(string.encode()).hexdigest()

silver, gold = "", ["#"] * 8
for i in range(int(1e9)):
	test_passwd = f"{data}{i}"
	hashed = md5(test_passwd)

	if hashed[:5] == "00000":
		if len(silver) < 8: silver += hashed[5]

		if (index := int(hashed[5], 16)) < 8:
			if gold[index] == "#": gold[index] = hashed[6]

		if "#" not in "".join(gold): break

print(f"Silver: {silver}\nGold: {''.join(gold)}")
