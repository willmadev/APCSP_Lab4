## Problem 12 - GRPH (Overlap Graphs)
## Willma
## 12/16/2020

## http://rosalind.info/problems/grph/

import resources
import copy

file_path = 'datasets/rosalind_grph.txt'
output_path = 'outputs/grph.txt'
dna_dict = resources.read_fasta(file_path)

k = 3

overlap = []
#for each dna seq, check last 3 nt with first 3 nt of each other dna seq
for dna in dna_dict:
    temp = copy.copy(dna_dict)
    temp.pop(dna)
    for other_dna in temp:
        suffix = dna_dict[dna][len(dna_dict[dna]) - k:]
        prefix = temp[other_dna][:k]
        if suffix == prefix:
            overlap.append([dna, other_dna])

overlap_formatted = []
for pair in overlap:
    overlap_formatted.append(resources.list_to_str(pair))

resources.write_file(output_path, overlap_formatted)