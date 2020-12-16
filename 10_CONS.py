## Problem 10 - CONS (Consensus and Profile)
## Willma
## 12/16/2020

## http://rosalind.info/problems/cons/

import resources

file_path = 'datasets/rosalind_cons.txt'
dna_dict = resources.read_fasta(file_path)

matrix = []
for dna_seq in dna_dict.values():
    matrix.append(dna_seq)

length = len(matrix[0])

#for each position add all the nts
A, C, G, T = [], [], [], []
consensus = ''
j = 0
while j < length:
    #create index j in each list
    A.append(0)
    C.append(0)
    G.append(0)
    T.append(0)

    for dna_seq in matrix:
        if dna_seq[j] == 'A':
            A[j] += 1
        elif dna_seq[j] == 'C':
            C[j] += 1
        elif dna_seq[j] == 'G':
            G[j] += 1
        elif dna_seq[j] == 'T':
            T[j] += 1
    
    #consensus string
    compareDict = {'A':A[j], 'C':C[j], 'G':G[j], 'T':T[j]}
    consensus += max(compareDict, key=compareDict.get)
    
    j += 1

output_list = [consensus, "A: " + resources.list_to_str(A), "C: " + resources.list_to_str(C), \
    "G: " + resources.list_to_str(G), "T: " + resources.list_to_str(T)]
output_path = 'outputs/cons.txt'
resources.write_file(output_path, output_list)