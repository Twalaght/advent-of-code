#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

silver, gold = 0, 0
for entry in data:
	nums = [""] * 10
	signal = ["".join(sorted(i)) for i in entry.split("|")[0].split()]

	# Find 1, 4, 7, 8
	for x in signal:
		unique_map = {2: 1, 3: 7, 4: 4, 7: 8}
		if len(x) in unique_map: nums[unique_map[len(x)]] = x

	for x in unique_map.values(): signal.remove(nums[x])

	# Finds 9
	for x in signal:
		tmp = set(sorted([char for char in nums[1] + nums[4] + nums[7]]))
		if set(tmp) <= set(x) and len(x) != 7: nums[9] = x

	signal.remove(nums[9])

	# Find 5 and 6
	for x in signal:
		if set(nums[4]).difference(set(nums[1])) <= set(x):
			nums[6 if set(nums[8]).difference(set(nums[9])) <= set(x) else 5] = x

	for x in [nums[5], nums[6]]: signal.remove(x)

	# Find 0
	for x in signal:
		if len(x) == 6: nums[0] = x

	signal.remove(nums[0])

	# Find 2 and 3
	for x in signal: nums[2 if set(nums[8]).difference(set(nums[9])) <= set(x) else 3] = x

	signal = [nums.index(x) for x in ["".join(sorted(x)) for x in entry.split("|")[1].split()]]
	silver += sum([signal.count(x) for x in [1, 4, 7, 8]])
	gold += int("".join([str(x) for x in signal]))

print(f"Silver: {silver}\nGold: {gold}")
