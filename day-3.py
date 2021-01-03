"""
Created on Thu Dec 24 02:11:58 2020

@author: ufukeskici
"""

import os
os.chdir('D:\\github\\advent-of-code-2020')

moveright = 3
movedown = 1
i = 0

# Calculate the number of rows
with open('day-3-map.txt', 'r') as f:
    rows = len(f.readlines())
    print(rows)
 
# Calculate the number of characters per line
with open('map.txt', 'r') as f:
    column = len(f.readline()) - 1
    print(column)

with open('map.txt', 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        i = i + moveright
        
        if i == 3:
            continue
        
        
        print(line)
#       line = line.split(' ')
#         policy = line[0].split('-')
#         letter = line[1].split(':')
#         password = str(line[2])
            
# print(f"The answer of part one is {n}")
# print(f"The answer of part two is {m}")

# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.