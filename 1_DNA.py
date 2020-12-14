## Problem 1 -file_pathWillma
## 12/14/2020

## http://rosalind.info/problems/dna/

import stuff

# Enter DNA Sequence here
file_path = 'datasets/rosalind_dna.txt'

dna_seq = stuff.read_file(file_path)

A, G, C, T = 0, 0, 0, 0

for nt in dna_seq:
    if nt == 'A':
        A += 1
    elif nt == 'G':
        G += 1
    elif nt == 'C':
        C += 1
    elif nt == 'T':
        T += 1

print(A,C,G,T)