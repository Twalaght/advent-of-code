#!/usr/bin/python3

import sys
from hashlib import md5
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().strip()

silver, gold = 0, 0
for i in range(int(1e9)):
	hashed = md5(f"{data}{i}".encode("utf-8")).hexdigest()
	if hashed[:5] == "00000" and silver == 0: silver = i
	if hashed[:6] == "000000":
		gold = i
		break

print(f"Silver: {silver}\nGold: {gold}")
