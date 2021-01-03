# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 02:11:58 2020

@author: ufukeskici
"""

import os
os.chdir('D:\\github\\advent-of-code-2020')

n = 0 # number of valid passwords for part 1
m = 0 # number of valid passwords for part 2

with open('day-2-password-list.txt', 'r') as f:
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