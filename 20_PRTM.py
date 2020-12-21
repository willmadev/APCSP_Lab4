## Problem 20 - PRTM (Calculating Protein Mass)
## Willma
## 12/21/2020

## http://rosalind.info/problems/prtm/

import resources

def PRTM(prot_string):
    '''
    Input: Protein String \n
    Output: total weight of protein string
    '''
    total_mass = 0
    for prot in prot_string:
        total_mass += resources.monoisotopic_mass_dict[prot]
    
    return(total_mass)

if __name__ == "__main__":
    file_path = 'datasets/rosalind_prtm.txt'
    prot_string = resources.read_file(file_path).strip('\n')
    print(PRTM(prot_string))