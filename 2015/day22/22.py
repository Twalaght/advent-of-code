#!/usr/bin/python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
	data = [x for x in f.read().splitlines()]

boss = [int(x.split()[-1]) for x in data]

def fight(spent, hp, mana, effects, boss_hp, boss_dam, turn, best, gold):
	# Early exit condition
	if spent > best: return int(1e7)

	if gold and turn % 2 == 0: hp -= 1

	# Shield
	if effects[0] > 0:
		effects[0] -= 1
	# Poison
	if effects[1] > 0:
		boss_hp -= 3
		effects[1] -= 1
	# Recharge
	if effects[2] > 0:
		mana += 101
		effects[2] -= 1

	if hp <= 0: return int(1e7)
	if boss_hp <= 0: return spent

	# If player turn
	if turn % 2 == 0:
		# Magic missle
		if mana >= 53:
			res = fight(spent + 53, hp, mana - 53, effects.copy(), boss_hp - 4, boss_dam, turn + 1, best, gold)
			best = min(best, res)

		# Drain
		if mana >= 73:
			res = fight(spent + 73, hp + 2, mana - 73, effects.copy(), boss_hp - 2, boss_dam, turn + 1, best, gold)
			best = min(best, res)

		# Shield
		if mana >= 113 and effects[0] == 0:
			tmp = effects.copy()
			tmp[0] = 6
			res = fight(spent + 113, hp, mana - 113, tmp, boss_hp, boss_dam, turn + 1, best, gold)
			best = min(best, res)

		# Poison
		if mana >= 173 and effects[1] == 0:
			tmp = effects.copy()
			tmp[1] = 6
			res = fight(spent + 173, hp, mana - 173, tmp, boss_hp, boss_dam, turn + 1, best, gold)
			best = min(best, res)

		# Recharge
		if mana >= 229 and effects[2] == 0:
			tmp = effects.copy()
			tmp[2] = 5
			res = fight(spent + 229, hp, mana - 229, tmp, boss_hp, boss_dam, turn + 1, best, gold)
			best = min(best, res)

		return best

	# Boss turn
	else:
		hp -= boss_dam if effects[0] == 0 else max(boss_dam - 7, 1)
		return fight(spent, hp, mana, effects.copy(), boss_hp, boss_dam, turn + 1, best, gold)

silver = fight(0, 50, 500, [0, 0, 0], boss[0], boss[1], 0, int(1e7), False)
gold = fight(0, 50, 500, [0, 0, 0], boss[0], boss[1], 0, int(1e7), True)
print(f"Silver: {silver}\nGold: {gold}")
