#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

counter = 0
arry = [2, 3, 4, 7]
for i in data:
	tmp = i.split("|")[1].split()
	for x in tmp:
		if len(x) in arry:
			counter += 1

print(f"Silver: {counter}")

len_map = {2: [1],
			3: [7],
			4: [4],
			5: [2, 3, 5],
			6: [0, 6, 9],
			7: [8]
			}

counter = 0

for dat in data:
	outstr = ""
	test = dat.split("|")[0].split()
	nums = [""] * 10

	for i in range(len(test)):
		test[i] = "".join(sorted(test[i]))

	# Finds 1, 4, 7, 8
	for i in test:
		if len(i) in [2, 3, 4, 7]:
			nums[len_map[len(i)][0]] = i

	test.remove(nums[1])
	test.remove(nums[4])
	test.remove(nums[7])
	test.remove(nums[8])

	# Finds 9
	for i in test:
		tmp = nums[1] + nums[4] + nums[7]
		tmp = sorted([char for char in tmp])
		tmp = set(tmp)


		if set(tmp) <= set(i) and len(i) != 7:
			nums[9] = i

	test.remove(nums[9])

	# Find bottom left segment
	bl_bit = set(nums[8]).difference(set(nums[9]))

	# Find 4 bar bit
	fourbar = set(nums[4]).difference(set(nums[1]))

	# Find 5 and 6
	for i in test:
		if fourbar <= set(i):
			if bl_bit <= set(i):
				nums[6] = i
			else:
				nums[5] = i

	test.remove(nums[5])
	test.remove(nums[6])

	# Find 0
	for i in test:
		if len(i) == 6:
			nums[0] = i

	test.remove(nums[0])

	# Find 2, 3
	for i in test:
		if bl_bit <= set(i):
			nums[2] = i
		else:
			nums[3] = i

	test.remove(nums[2])
	test.remove(nums[3])

	test = dat.split("|")[1].split()
	for i in range(len(test)):
		test[i] = "".join(sorted(test[i]))

	for t in test:
		for i in range(10):
			if t == nums[i]:
				outstr += str(i)

	counter += int(outstr)

print(f"Gold: {counter}")
