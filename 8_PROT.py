## Problem 8 - PROT (Translating RNA into Protein)
## Willma
## 12/16/2020

## http://rosalind.info/problems/prot/

import resources

def PROT(rna):
    '''
    Input: RNA string \n
    Output: Protein string
    '''
    i=0
    prot = ''
    while i < len(rna):
        window = rna[i:i+3]
        prot += resources.codonDict[window]
        i+=3

    return(prot.strip('*'))

if __name__ == "__main__":
    file_path = 'datasets/rosalind_prot.txt'
    rna = resources.read_file(file_path).strip()
    print(PROT(rna))