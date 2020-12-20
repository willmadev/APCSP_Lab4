## Problem 7 - HAMM (Counting Point Mutations)
## Willma
## 12/16/2020

## http://rosalind.info/problems/hamm/

import resources

def HAMM(s,t):
    '''
    Input: 2 DNA strings of equal length\n
    Output: Hamming distance
    '''
    hamm, i = 0, 0
    while i < len(s):
        if s[i] != t[i]:
            hamm += 1
        i += 1

    return(hamm)

if __name__ == "__main__":
    file_path = 'datasets/rosalind_hamm.txt'
    s, t = [str(data) for data in resources.read_file(file_path).strip('\n').split('\n')]
    print(HAMM(s, t))