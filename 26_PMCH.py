## Problem 26 - PMCH (Perfect Matchings and RNA Secondary Structures)
## Willma
## 1/11/2021

## http://rosalind.info/problems/pmch/

import resources

class Node():
    def __init__(self, nt):
        self.nt = nt
        self.basepair_edges = []

    def __repr__(self):
        return self.nt

def PMCH(rna_seq):
    # create bonding graph
    bonding_graph = []
    for nt in rna_seq:
        bonding_graph.append(Node(nt))
    
    for nt in bonding_graph:
        corr_nt = resources.rna_compliments[nt.nt]
        # only do half of the base pairs
        if corr_nt == 'U' or corr_nt == 'G':
            continue

        for nt2 in bonding_graph:
            if nt2.nt == corr_nt:
                nt.basepair_edges.append(nt2)
                nt2.basepair_edges.append(nt)

    for nt in bonding_graph:
        print(nt.nt, nt.basepair_edges)

        
    # find total possible perfect matchings

if __name__ == "__main__":
    PMCH('AGCUAGUCAU')