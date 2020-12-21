## Problem 21 - REVP (Locating Restriction Sites)
## Willma
## 12/21/2020

## http://rosalind.info/problems/revp/

import resources
import math

def REVP(dna_dict):
    '''
    Input: Dict with description as key and dna sequence as value \n
    Output: Writes list of position and length of all reverse palindromes 
    of length 4-12 to outputs/revp.txt
    '''
    #get dna sequence
    dna_seq = resources.fasta_to_string(dna_dict)[1]

    #get compliment
    compliment = ''
    for nt in dna_seq:
        compliment += resources.compliments[nt]
    
    revp = []
    #for each starting location in dna sequence
    for i in range(len(dna_seq)):
        #test each length from 4 to 12
        for length in range(3,12):
            #if length is longer than dna seq skip
            if i + length + 1 > len(dna_seq):
                break
            
            pal = False
            #test if that length is a palindrome
            for pal_index in range(length):
                if dna_seq[i+pal_index] == compliment[i+length-pal_index]:
                    pal = True
                else:
                    pal = False
                    break

            if pal:
                revp.append([i + 1, length + 1])
    
    #convert to string
    revp = [resources.list_to_str(pair).strip() for pair in revp]
    
    output_path = 'outputs/revp.txt'
    resources.write_file(output_path, revp)

if __name__ == "__main__":
    file_path = 'datasets/rosalind_revp.txt'
    fasta_dict = resources.read_fasta(file_path)
    REVP(fasta_dict)