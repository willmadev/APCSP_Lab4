## Problem 11 - FIBD (Mortal Fibonacci Rabbits)
## Willma
## 12/16/2020

## http://rosalind.info/problems/fibd/

import resources
import copy


file_path = 'datasets/rosalind_fibd.txt'
n, m = [int(x) for x in resources.read_file(file_path).strip('\n').split()]

i = 0

rabbits = {0:1}
while i < n-1:
    temp_rabbits = copy.copy(rabbits)
    for age in temp_rabbits:
        if age == 0:
            rabbits[1] = temp_rabbits[0]
            rabbits[0] = 0
        elif age >= 1:
            rabbits[age + 1] = temp_rabbits[age]
            rabbits[0] += temp_rabbits[age]
            if age + 1 == m:
                rabbits[m] = 0

    i+=1

total = 0
for age in rabbits:
    if age != m:
        total += rabbits[age]

print(total)