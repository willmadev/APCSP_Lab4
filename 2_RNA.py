## Problem 2 -file_pathWillma
## 12/14/2020

## http://rosalind.info/problems/rna/

import stuff

# Enter DNA Sequence here
file_path = 'datasets/rosalind_rna.txt'

dna_seq = stuff.read_file(file_path)

rna_seq = ''

for nt in dna_seq:
    if nt == 'T':
        rna_seq += 'U'
    else:
        rna_seq += nt

print(rna_seq)