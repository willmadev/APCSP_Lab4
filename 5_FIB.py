## Problem 5 - FIB (Rabbits and Recurrence Relations)
## Willma
## 12/14/2020

## http://rosalind.info/problems/iprb/

import stuff
import math

n, k = [int(data) for data in stuff.read_file('datasets/rosalind_fib.txt').split(' ')]

i = 0
children, adults = 1, 0
while i < n-1:
    temp = children
    children = adults * k
    adults += temp
    i+=1

print(adults + children)