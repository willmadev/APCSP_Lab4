## Problem 14 - LCSM (Finding a Shared Motif)
## Willma
## 12/16/2020

## http://rosalind.info/problems/lcsm/

import resources

def LCSM(dna_list):
    '''
    Input: List of DNA strings \n
    Output: Longest common substring
    '''

    longest_substring = ''
    start_loc = 0
    nt = 0
    while nt < len(dna_list[0]):
        end_loc = nt
        substring_works = True
        while substring_works == True:
            substring = dna_list[0][nt:end_loc]

            for dna in dna_list:
                #if substring is not in dna
                if dna.find(substring) == -1:
                    substring_works = False
            
            #if substring is in all dna
            if substring_works == True:
                if len(substring) > len(longest_substring):
                    longest_substring = substring
                end_loc += 1
                if end_loc > len(dna_list[0]):
                    substring_works = False
        nt += 1
    return(longest_substring)

if __name__ == "__main__":
    file_path = 'datasets/rosalind_lcsm.txt'
    dna_list = [data for data in resources.read_fasta(file_path).values()]

    print(LCSM(dna_list))