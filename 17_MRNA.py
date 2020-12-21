## Problem 17 - MRNA (Inferring mRNA from Protein)
## Willma
## 12/21/2020

## http://rosalind.info/problems/mrna/

import resources

def MRNA(protein_seq):
    '''
    Input: Protein string \n
    Output: Total number of RNA strings the protein could have been translated from, modulo 1,000,000
    '''
    n=1000000
    possiblities = 1
    for prot in protein_seq:
        possiblities *= len(resources.aaDict[prot])
    
    possiblities = possiblities * len(resources.aaDict['*'])
    return possiblities % n

if __name__ == "__main__":
    file_path = 'datasets/rosalind_mrna.txt'
    protein_seq = resources.read_file(file_path).strip('\n')
    print(MRNA(protein_seq))