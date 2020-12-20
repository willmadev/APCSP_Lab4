## Problem 4 - IPRB (Mendel's First Law)
## Willma
## 12/14/2020

## http://rosalind.info/problems/iprb/

import resources


def IPRB(k, m, n):
    '''
    Input: (homozygous dominant, heterozygous, homozygous recessive) \n
    Output: The probability that two randomly selected mating organisms 
    will produce an individual possessing a dominant allele (and thus displaying 
    the dominant phenotype). Assume that any two organisms can mate.
    '''
    #dom, het, rec
    
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

    return(total_dom)

if __name__ == "__main__":
    file_path = 'datasets/rosalind_iprb.txt'
    k, m, n = resources.read_file(file_path).split(' ')
    print(IPRB(k, m, n))