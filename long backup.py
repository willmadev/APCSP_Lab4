## Problem 25 - LONG (Genome Assembly as Shortest Superstring)
## Willma
## 1/5/2021

## http://rosalind.info/problems/long/

import resources
import math
import copy

def LONG(dna_dict):
    dna_list = [read for read in dna_dict.values()]
    tail_list = copy.copy(dna_list)
    ordered_list = [dna_list[0]]

    # order the list
    for read in dna_list:
        min_head_length = math.ceil(len(read) / 2)
        min_head = read[:min_head_length]
        has_corr_tail = False

        if read not in ordered_list:
            ordered_list.append(read)
        order_index = ordered_list.index(read)

        # remove from tail options
        if read in tail_list:
            in_tail_list = True
            tail_list.remove(read)
        else:
            in_tail_list = False

        for tail_read in tail_list:
            if min_head not in tail_read:
                continue

            loc = tail_read.find(min_head)
            tail = tail_read[loc:]

            if tail not in read:
                continue

            # if matching
            if tail_read in ordered_list:
                ordered_list.remove(read)
                order_index = ordered_list.index(tail_read)
                ordered_list.insert(order_index+1, read)
            else:
                ordered_list.insert(order_index, tail_read)

            tail_list.remove(tail_read)
            has_corr_tail = True
            break

        # if read has no matching tail its the first read
        if not has_corr_tail:
            ordered_list.remove(read)
            ordered_list.insert(0, read)

        # add back to tail list
        if in_tail_list:
            tail_list.append(read)

    # combine into supersting
    superstring = ''
    for i in range(len(ordered_list)):
        if i == 0:
            superstring = ordered_list[i]
            continue
        
        read = ordered_list[i]

        min_head_length = math.ceil(len(read) / 2)
        min_head = read[:min_head_length]
        
        prev_read = ordered_list[i-1]
        loc = prev_read.find(min_head)
        tail = prev_read[loc:]

        superstring += read[len(tail):]

    output_path = 'outputs/long.txt'
    resources.write_file(output_path, [superstring])


    # old code
        # # for each seq find another seq whose tail matches their head
        # # working backwards
        # superstring = ''
        # head_seq_list = [seq for seq in dna_dict.values()]
        # tail_seq_list = copy.copy(head_seq_list)
        # overlap_length = math.ceil(len(head_seq_list[0])/2)

        # head_seq = head_seq_list[0]
        # while True:
        #     print(head_seq_list)
        #     print(tail_seq_list)

        #     min_head = head_seq[:overlap_length]
        #     has_corr_tail = False
            
        #     if head_seq in tail_seq_list:
        #         in_tail_list = True
        #         tail_seq_list.remove(head_seq)

        #     # compare with each tail
        #     for tail_seq in tail_seq_list:
        #         # find head in tail sequence
        #         tail_loc = tail_seq.find(min_head)
        #         if tail_loc == -1:
        #             continue
                
        #         # check if entire tail sequence is in head
        #         tail = tail_seq[tail_loc:]
        #         if tail not in head_seq:
        #             continue
        #         else:
        #             # add to superstring, remove from tail list, set as new head seq
        #             superstring = tail_seq[:tail_loc] + head_seq + superstring
        #             print(superstring)
        #             has_corr_tail = True
        #             tail_seq_list.remove(tail_seq)
        #             head_seq_list.remove(head_seq)
        #             head_seq = tail_seq
        #             break
            
        #     if not has_corr_tail:
        #         head = head_seq
        #         head_seq_list.remove(head_seq)
                
        #         if len(head_seq_list) == 0:
        #             break

        #         head_seq = head_seq_list[0]
            
        #     if len(head_seq_list) == 0:
        #         break  

        # print(superstring)
            


if __name__ == "__main__":
    file_path = 'datasets/rosalind_long.txt'
    dna_dict = resources.read_fasta(file_path)
    LONG(dna_dict)
