## Problem 2 - RNA (Transcribing DNA into RNA)
## Willma
## 12/14/2020

## http://rosalind.info/problems/rna/

import resources

def RNA(dna_seq):
    '''
    Input: DNA Sequence \n
    Output: RNA Sequence
    '''
    rna_seq = ''

    for nt in dna_seq:
        if nt == 'T':
            rna_seq += 'U'
        else:
            rna_seq += nt

    return(rna_seq)

if __name__ == "__main__":
    file_path = 'datasets/rosalind_rna.txt'
    dna_seq = resources.read_file(file_path)

    print(RNA(dna_seq))