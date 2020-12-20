## Problem 5 - FIB (Rabbits and Recurrence Relations)
## Willma
## 12/14/2020

## http://rosalind.info/problems/fib/

import resources
import math

def FIB(n,k):
    '''
    Input: n = Months, k = rabbit pairs produced by reproduction-age rabbit pairs \n
    Output: Total population after n months
    '''
    i = 0
    children, adults = 1, 0
    while i < n-1:
        temp = children
        children = adults * k
        adults += temp
        i+=1

    return(adults + children)

if __name__ == "__main__":
    n, k = [int(data) for data in resources.read_file('datasets/rosalind_fib.txt').split(' ')]
    print(FIB(n, k))