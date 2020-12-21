## Problem 15 - LIA (Independent Alleles)
## Willma
## 12/21/2020

## http://rosalind.info/problems/lia/

# TODO: idk how to doooo ask deranek
import resources

def LIA(k,n):
     #AABB = 1/16
     #AABb = 2/16
     #AaBB = 2/16
     #AaBb = 4/16
     #AAbb = 1/16
     #Aabb = 2/16
     #aaBB = 1/16
     #aaBb = 2/16
     #aabb = 1/16

     #AA = 1/4
     #Aa = 2/4
     #aa = 1/4

     generation = 0
     while generation < k:
          # Pr(AA) * Pr(Aa)
     generation += 1

if __name__ == "__main__":
     file_path = 'datasets/rosalind_lia.txt'
     k, n = [data for data in resources.read_file(file_path).strip('\n').split()]
