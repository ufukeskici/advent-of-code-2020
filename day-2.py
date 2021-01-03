# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 02:11:58 2020

@author: ufukeskici
"""

import os
os.chdir('D:\\github\\advent-of-code-2020\\day-2')

n = 0 # number of valid passwords for part 1
m = 0 # number of valid passwords for part 2

with open('password_list.txt', 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        line = line.split(' ')
        policy = line[0].split('-')
        letter = line[1].split(':')
        password = str(line[2])

        # solution of part 1
        
        if int(policy[0]) <= password.count(letter[0]) <= int(policy[1]):
            n = n + 1
            
        # solution of part 2
        
        if password[int(policy[0])-1] == letter[0] or password[int(policy[1])-1] == letter[0]:
            m = m + 1
        
        if password[int(policy[0])-1] == letter[0] and password[int(policy[1])-1] == letter[0]:
            m = m - 1
            
print(f"The answer of part one is {n}")
print(f"The answer of part two is {m}")

# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
