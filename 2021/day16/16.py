#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().strip()

input_str = "".join([bin(int(x, 16))[2:].zfill(4) for x in data])

def literal(string):
	num = ""
	while(True):
		five = string[:5]
		string = string[5:]
		num += five[1:]
		if five[0] == "0": break

	return int(num, 2), string

def ops(inputs, op):
	if op == 0: return sum(inputs)
	if op == 1:
		gold = 1
		for x in inputs: gold *= x
		return gold
	if op == 2: return min(inputs)
	if op == 3: return max(inputs)
	if op == 5: return inputs[0] > inputs[1]
	if op == 6: return inputs[0] < inputs[1]
	if op == 7: return inputs[0] == inputs[1]

def parse(string):
	version = int(string[:3], 2)
	type_id = int(string[3:6], 2)
	string = string[6:]
	silver = version

	if type_id == 4:
		num, string = literal(string)
		return num, version, string

	len_type = int(string[0], 2)
	bitlen = 15 if len_type == 0 else 11
	length = int(string[1:bitlen + 1], 2)
	string = string[bitlen + 1:]

	inputs = []
	if len_type == 0:
		tmp = string[:length]
		string = string[length:]

		while tmp:
			in_num, ver_sum, tmp = parse(tmp)
			silver += ver_sum
			inputs.append(in_num)
	else:
		for i in range(length):
			in_num, ver_sum, string = parse(string)
			silver += ver_sum
			inputs.append(in_num)

	return ops(inputs, type_id), silver, string

gold, silver, bin_str = parse(input_str)
print(f"Silver: {silver}\nGold: {gold}")
