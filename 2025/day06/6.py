#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()
    silver_data = [x.split() for x in data]
    problems = []
    for i in range(len(silver_data[0])):
        problems.append([silver_data[row][i] for row in range(len(data))])
    
    gold_problems = []
    tmp_problem = []
    for i in range(len(data[0])):
        tmp = "".join([x for x in [data[row][i] for row in range(len(data))] if x.isnumeric()])
        if tmp:
            tmp_problem.append(tmp)
        else:
            gold_problems.append(tmp_problem)
            tmp_problem = []
        
    gold_problems.append(tmp_problem)

    # Steal operands from silver
    gold_problems = [
        [*gold_problems[i], problems[i][-1]] for i in range(len(gold_problems))
    ]

def solve(problems: list[list[str]]) -> int:
    total = 0
    for problem in problems:
        operand = problem[-1]
        if operand == "*":
            tmp = 1
            for item in problem[:-1]:
                tmp *= int(item)
            
            total += tmp

        if operand == "+":
            total += sum([int(x) for x in problem[:-1]])
    
    return total

silver = solve(problems)
gold = solve(gold_problems)

print(f"Silver: {silver}\nGold: {gold}")
