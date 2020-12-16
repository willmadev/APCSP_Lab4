## Problem 4 - IPRB (Mendel's First Law)
## Willma
## 12/14/2020

## http://rosalind.info/problems/iprb/

import stuff

#dom, het, rec
file_path = 'datasets/rosalind_iprb.txt'
k, m, n = stuff.read_file(file_path).split(' ')
k, m, n = int(k), int(m), int(n)
total = k + m + n

A_dom = k/total
A_het = m/total
A_rec = n/total

A_dom_B_dom = (k-1)/(total-1)
A_dom_B_het = m/(total-1)
A_dom_B_rec = n/(total-1)

A_het_B_dom = k/(total-1)
A_het_B_het = (m-1)/(total-1) * 0.75
A_het_B_rec = n/(total-1) * 0.5

A_rec_B_dom = k/(total-1)
A_rec_B_het = m/(total-1) * 0.5
A_rec_B_rec = (n-1)/(total-1)

total_dom = ((A_dom_B_dom * A_dom) + (A_dom_B_het * A_dom) + (A_dom_B_rec * A_dom) +
    (A_het_B_dom * A_het) + (A_het_B_het * A_het) + (A_het_B_rec * A_het) +
    (A_rec_B_dom * A_rec) + (A_rec_B_het * A_rec)
)

print(total_dom)