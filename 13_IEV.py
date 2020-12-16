## Problem 13 - IEV (Calculating Expected Offspring)
## Willma
## 12/16/2020

## http://rosalind.info/problems/iev/

import resources

file_path = 'datasets/rosalind_iev.txt'
DD, DH, DR, HH, HR, RR = [float(data) for data in resources.read_file(file_path).strip('\n').split()]

# DD - 100%
# DH - 100%
# DR - 100%
# HH - 75%
# HR - 50%
# RR - 0%

expected = (DD + DH + DR + HH * 0.75 + HR * 0.5) * 2
print(expected)