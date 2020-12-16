## Problem 2 - RNA (Transcribing DNA into RNA)
## Willma
## 12/14/2020

## http://rosalind.info/problems/rna/

import resources

# Enter DNA Sequence here
file_path = 'datasets/rosalind_rna.txt'

dna_seq = resources.read_file(file_path)

rna_seq = ''

for nt in dna_seq:
    if nt == 'T':
        rna_seq += 'U'
    else:
        rna_seq += nt

print(rna_seq)