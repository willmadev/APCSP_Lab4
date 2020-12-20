## Problem 9 - SUBS (Finding a Motif in DNA)
## Willma
## 12/16/2020

## http://rosalind.info/problems/subs/

import resources

def SUBS(s, t):
    '''
    Input: 2 DNA strings s,t
    Output: Locations of t as a substring of s (space separated list)
    '''
    loc = 0
    locs = [s.find(t) + 1]
    while True:
        loc = s.find(t, locs[len(locs) - 1])
        if loc == -1:
            break
        locs.append(loc + 1)

    locs_str = resources.list_to_str(locs)

    return(locs_str)

if __name__ == "__main__":
    file_path = 'datasets/rosalind_subs.txt'
    s, t =  [str(data) for data in resources.read_file(file_path).strip('\n').split('\n')]
    print(SUBS(s, t))
