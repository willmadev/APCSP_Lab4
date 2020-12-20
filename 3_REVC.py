## Problem 3 - REVC (Complementing a Strand of DNA)
## Willma
## 12/14/2020

## http://rosalind.info/problems/revc/

import resources

def REVC(dna_seq):
    '''
    Input: DNA Sequence \n
    Output: Reverse Compliment
    '''
    reverse = dna_seq[::-1]

    complements = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

    revc = ''
    for nt in reverse:
        revc += complements[nt]

    return(revc)

if __name__ == "__main__":
    file_name = 'datasets/rosalind_revc.txt'
    dna_seq = resources.read_file(file_name).strip('\n')
    print(REVC(dna_seq))