## Problem 9 - SUBS (Finding a Motif in DNA)
## Willma
## 12/16/2020

## http://rosalind.info/problems/prot/

import resources

file_path = 'datasets/rosalind_subs.txt'
s, t =  [str(data) for data in resources.read_file(file_path).strip('\n').split('\n')]

loc = 0
locs = [s.find(t) + 1]
while True:
    loc = s.find(t, locs[len(locs) - 1])
    if loc == -1:
        break
    locs.append(loc + 1)

locs_str = ''
for item in locs:
    locs_str += str(item) + ' '

print (locs_str)