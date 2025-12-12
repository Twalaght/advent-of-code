#!/usr/bin/env python3

import sys
import z3
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

def gen_presses(length: int) -> list[list[int]]:
    if length == 1:
        return [[0], [1]]
    
    tmp = gen_presses(length - 1)
    zero = [[0, *x] for x in tmp]
    ones = [[1, *x] for x in tmp]
    return [*zero, *ones]

silver, gold = 0, 0

for row in data:
    tmp = row.split(" ")
    end_state = tmp.pop(0)
    end = [x for x in end_state[1:-1]]
    joltage = [int(x) for x in tmp.pop(-1)[1:-1].split(",")]
    buttons = [[int(i) for i in x[1:-1].split(",")] for x in tmp]

    best = 999
    attempts = []
    for press_set in gen_presses(len(buttons)):
        tmp = ["." for _ in range(len(end))]
        for i in range(len(press_set)):
            if press_set[i]:
                for e in buttons[i]:
                    tmp[e] = "#" if tmp[e] == "." else "."

        if tmp == end:
            attempts.append(press_set)
    
    silver += min([sum(x) for x in attempts])

    # This is just a matrix problem, which is tricky in raw python,
    # but Z3 is just "import solution" honestly, good enough for me.
    solver = z3.Solver()
    button_vars = [z3.Int(f"a{n}") for n in range(len(buttons))]
    for b in button_vars:
        solver.add(b >= 0)

    for i, v in enumerate(joltage):
        joltage_vars = [button_vars[j] for j,button in enumerate(buttons) if i in button]
        solver.add(z3.Sum(joltage_vars) == v)

    while solver.check() == z3.sat:
        model = solver.model()
        n = sum([model[d].as_long() for d in model])
        solver.add(z3.Sum(button_vars) < n)

    gold += n

print(f"Silver: {silver}\nGold: {gold}")
