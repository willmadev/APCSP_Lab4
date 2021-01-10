## Problem 25 - LONG (Genome Assembly as Shortest Superstring)
## Willma
## 1/5/2021

## http://rosalind.info/problems/long/

import resources
import math
import copy
import json

def LONG(dna_dict):
    dna_list = [read for read in dna_dict.values()]
    tail_list = copy.copy(dna_list)

    corr_dict = {}

    # order the list
    for read in dna_list:
        min_head_length = math.ceil(len(read) / 2)
        min_head = read[:min_head_length]
        has_corr_tail = False

        # remove from tail options
        tail_list.remove(read)

        for tail_read in tail_list:
            if min_head not in tail_read:
                continue

            loc = tail_read.find(min_head)
            overlap = tail_read[loc:]

            if overlap not in read:
                continue
            
            # if matching
            corr_dict[tail_read] = read
            has_corr_tail = True

        # head
        if has_corr_tail == False:
            corr_dict['_head'] = read

        # add back to tail list
        tail_list.append(read)

    # combine into supersting
    # get head with no tail
    last_read = corr_dict['_head']
    superstring = last_read

    for i in range(len(corr_dict) - 1):
        # find corr tail
        sec_last_read = last_read
        last_read = corr_dict[sec_last_read]

        # find overlap
        min_head_length = math.ceil(len(last_read) / 2)
        min_head = last_read[:min_head_length]

        loc = sec_last_read.find(min_head)
        overlap = sec_last_read[loc:]
        
        # add to superstring
        superstring += last_read[len(overlap):]
    
    output_path = 'outputs/long.txt'
    resources.write_file(output_path, [superstring])            


if __name__ == "__main__":
    file_path = 'datasets/rosalind_long.txt'
    dna_dict = resources.read_fasta(file_path)
    LONG(dna_dict)
