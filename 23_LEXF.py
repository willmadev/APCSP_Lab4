## Problem 23 - LEXF (Enumerating k-mers Lexicographically)
## Willma
## 12/28/2020

## http://rosalind.info/problems/lexf/

import resources

def LEXF(alphabets, n):
    '''
    Input: list of alphabets, length \n
    Output: writes a list of strings of length that can be formed by alphabet lexicographically to outputs/lexf.txt
    '''
    n = int(n)
    permutation = []

    for letter in alphabets:
        permutation.append(letter)

    def permutations(prefix):
        temp_list = []
        for letter in alphabets:
            temp_list.append(prefix + str(letter))

        return temp_list
        
    for i in range(n-1):
        temp_list = []
        for prefix in permutation:
            for perm in permutations(prefix):
                temp_list.append(perm)
        
        permutation = temp_list
        
    output_path = 'outputs/lexf.txt'
    resources.write_file(output_path, permutation)

if __name__ == "__main__":
    file_path = 'datasets/rosalind_lexf.txt'
    alphabets, n = resources.read_file(file_path).strip('\n').split('\n')
    alphabets = [letter for letter in alphabets.split()]
    
    LEXF(alphabets, n)