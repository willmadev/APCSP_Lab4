## Problem 5 - GC (Computing GC Content)
## Willma
## 12/16/2020

## http://rosalind.info/problems/gc/

import resources

def GC(dna_dict):
    '''
    Input: Fasta Dictionary with ID as key and DNA sequence as value \n
    Output: ID of sequence with highest GC content, GC content
    '''
    gc_content = dict()
    for sample in dna_dict:
        sequence = str(dna_dict[sample])
        G = sequence.count('G')
        C = sequence.count('C')

        gc_content[sample] = (G + C) / len(sequence) * 100

    max_gc = max(gc_content, key=gc_content.get)

    return(max_gc, gc_content[max_gc])

if __name__ == "__main__":
    file_path = 'datasets/rosalind_gc.txt'
    dna_dict = resources.read_fasta(file_path)
    print(GC(dna_dict))