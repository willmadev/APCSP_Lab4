## Problem 15 - LIA (Independent Alleles)
## Willma
## 12/21/2020

## http://rosalind.info/problems/lia/

# TODO: idk how to doooo ask deranek
import resources
import numpy as np
from scipy.stats import binom
import math

# works cited
# https://en.wikipedia.org/wiki/Combination
# 

def ncr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))


def LIA(k,N):
     p = 1/4        # probability of success on a single trial
     n = 2 ** k     # number of trials
     prob = []      # summation solutions
     for x in range(N, n):
          prob.append(binom.cdf(ncr(2**k, x), n, p))

     return sum(prob)

if __name__ == "__main__":
     # file_path = 'datasets/rosalind_lia.txt'
     # k, n = [data for data in resources.read_file(file_path).strip('\n').split()]
     print(LIA(2, 1))
