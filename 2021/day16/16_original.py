#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = f.read().splitlines()

bin_str = ""
for i in data[0]:
	test = bin(int(i, 16))[2:]
	test = test.zfill(4)
	bin_str += test

def literal(string):
	num = ""
	while(True):
		five = string[:5]
		string = string[5:]
		num += five[1:]
		if five[0] == "0": break

	return int(num, 2), string

def parse(string):
	silver = 0
	gold = 0
	version = int(string[:3], 2)
	type_id = int(string[3:6], 2)
	string = string[6:]

	if type_id == 4:
		num, string = literal(string)
		return num, version, string

	len_type = int(string[0], 2)
	string = string[1:]

	length = 0
	if len_type == 0:
		length = int(string[:15], 2)
		string = string[15:]
	else:
		length = int(string[:11], 2)
		string = string[11:]

	gold_arry = []
	if len_type == 0:
		tmp = string[:length]
		string = string[length:]

		while tmp:
			tmp_gold, tmp_silver, tmp = parse(tmp)
			silver += tmp_silver
			gold_arry.append(tmp_gold)
	else:
		for i in range(length):
			tmp_gold, tmp_silver, string = parse(string)
			silver += tmp_silver
			gold_arry.append(tmp_gold)

	if type_id == 0:
		gold = sum(gold_arry)
	elif type_id == 1:
		gold = 1
		for i in gold_arry:
			gold *= i
	elif type_id == 2:
		gold = min(gold_arry)
	elif type_id == 3:
		gold = max(gold_arry)
	elif type_id == 5:
		if gold_arry[0] > gold_arry[1]:
			gold = 1
		else:
			gold = 0
	elif type_id == 6:
		if gold_arry[0] < gold_arry[1]:
			gold = 1
		else:
			gold = 0
	elif type_id == 7:
		if gold_arry[0] == gold_arry[1]:
			gold = 1
		else:
			gold = 0

	silver += version
	return gold, silver, string

gold, silver, bin_str = parse(bin_str)
print(f"Silver: {silver}\nGold: {gold}")
