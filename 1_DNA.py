## Problem 1 - DNA (Counting DNA Nucleotides)
## Willma
## 12/14/2020

## http://rosalind.info/problems/dna/

import resources

# Enter DNA Sequence here
file_path = 'datasets/rosalind_dna.txt'

dna_seq = resources.read_file(file_path)

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