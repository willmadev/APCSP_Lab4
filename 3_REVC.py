## Problem 3 - REVC
## Willma
## 12/14/2020

## http://rosalind.info/problems/revc/

import stuff

# Enter DNA Sequence here
file_name = 'datasets/rosalind_revc.txt'

dna_seq = stuff.read_file(file_name).strip('\n')

reverse = dna_seq[::-1]

complements = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

revc = ''
for nt in reverse:
    revc += complements[nt]

print(revc)