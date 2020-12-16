## Problem 3 - REVC (Complementing a Strand of DNA)
## Willma
## 12/14/2020

## http://rosalind.info/problems/revc/

import resources

# Enter DNA Sequence here
file_name = 'datasets/rosalind_revc.txt'

dna_seq = resources.read_file(file_name).strip('\n')

reverse = dna_seq[::-1]

complements = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

revc = ''
for nt in reverse:
    revc += complements[nt]

print(revc)