## Problem 5 - GC (Computing GC Content)
## Willma
## 12/16/2020

## http://rosalind.info/problems/gc/

import resources

file_path = 'datasets/rosalind_gc.txt'
dna_dict = resources.read_fasta(file_path)

gc_content = dict()
for sample in dna_dict:
    sequence = str(dna_dict[sample])
    G = sequence.count('G')
    C = sequence.count('C')

    gc_content[sample] = (G + C) / len(sequence) * 100

max_gc = max(gc_content, key=gc_content.get)
print(max_gc)
print(gc_content[max_gc])