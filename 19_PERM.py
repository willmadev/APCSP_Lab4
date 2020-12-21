## Problem 18 - PERM (Enumerating Gene Orders)
## Willma
## 12/21/2020

## http://rosalind.info/problems/perm/

import resources
import copy

def permutations(num_list):
    '''
    Input: list of numbers \n
    Output: Permutations of list
    '''
    #if list is empty return empty list
    if len(num_list) == 0:
        return []
    # if list has one item return list with one item
    if len(num_list) == 1:
        return num_list
    
    # if list has multiple items
    # save the first digit and put the rest through this function
    return_list = []
    for i in num_list:
        temp_list = copy.copy(num_list)
        temp_list.remove(i)
        
        perm_list = permutations(temp_list)
        for perm in perm_list:
            something = [i]
            if type(perm) == list:
                for item in perm:
                    something.append(item)
            else:
                something.append(perm)
            return_list.append(something)
    
    return(return_list)

def PERM(n):
    '''
    Input: length of permutations \n
    Output: Writes list of permutations to 'outputs/perm.txt'
    '''
    num_list = [i+1 for i in range(n)]
    perm_list = permutations(num_list)
    formatted_list = [resources.list_to_str(perm).strip() for perm in perm_list]
    formatted_list.insert(0, str(len(perm_list)))
    
    output_path = 'outputs/perm.txt'
    resources.write_file(output_path, formatted_list)
    


if __name__ == "__main__":
    file_path = 'datasets/rosalind_perm.txt'
    n = int(resources.read_file(file_path).strip('\n'))
    PERM(n)