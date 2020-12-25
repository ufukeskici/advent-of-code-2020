# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 02:11:58 2020

@author: ufukeskici
"""
# solution of part 1

import os
os.chdir('D:\\github\\advent-of-code-2020\\day-1')

expenses = []

with open('expense_report.txt', 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        expenses.append(int(line))

for i in expenses:
    x = 2020 - i
    if x in expenses:
        solution1 = x * i
    
print(f"The answer of part one is {solution1}")

# solution of part 2

for a in expenses:
    for b in expenses:
        c = 2020 - (a + b)
        if c in expenses:
            solution2 = a * b * c

print(f"The answer of part two is {solution2}")