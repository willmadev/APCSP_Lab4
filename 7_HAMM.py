## Problem 7 - HAMM (Counting Point Mutations)
## Willma
## 12/16/2020

## http://rosalind.info/problems/hamm/

import resources

file_path = 'datasets/rosalind_hamm.txt'
s, t = [str(data) for data in resources.read_file(file_path).strip('\n').split('\n')]

hamm, i = 0, 0
while i < len(s):
    if s[i] != t[i]:
        hamm += 1
    i += 1

print(hamm)