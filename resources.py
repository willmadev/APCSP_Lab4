def read_file(file_path):
    '''
    Input: file path \n
    Output: string of data in file
    '''
    with open(file_path) as f:
        file_data = f.read()
    return file_data

def read_fasta(file_path):
    #setup variables
    key = str()
    sequence = str()
    dictionary = dict()

    with open(file_path) as f:
        #carry out for each line
        for line in f:

            #if the line starts with > save the rest of the line as the key
            if line[0] == ">":
                #
                if(key != ""):
                    dictionary[key] = sequence
                    key = str()
                    sequence = str()
                key = line[1:].strip("\n")
            else:
                sequence = sequence + line.strip("\n")
            #add this line to the existing sequence
            

            #if the file doesn't end with a \n
        if key not in dictionary.keys():
            dictionary[key] = sequence
    
    return(dictionary)

def write_file(file_path, strList):
    with open(file_path, 'w') as f:
        for string in strList:
            f.write(string + '\n')

codonDict = {
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'UUA': 'L', 'UUG': 'L',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'UUU': 'F', 'UUC': 'F', 'AUG': 'M', 'UGU': 'C', 'UGC': 'C',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G', 'CCU': 'P',
    'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'UCU': 'S', 'UCC': 'S',
    'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S', 'UAU': 'Y', 'UAC': 'Y', 'UGG': 'W', 'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N', 'CAU': 'H', 'CAC': 'H', 'GAA': 'E', 'GAG': 'E', 'GAU': 'D', 'GAC': 'D', 'AAA': 'K',
    'AAG': 'K', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R', 'UAA': '*', 'UAG': '*',
    'UGA': '*'
}

aaDict = {
    'A': ['GCU', 'GCC', 'GCA', 'GCG'], 'C': ['UGU', 'UGC'], 'D': ['GAU', 'GAC'], 'E': ['GAA', 'GAG'], 
    'F': ['UUU', 'UUC'], 'G': ['GGU', 'GGC', 'GGA', 'GGG'], 'H': ['CAU', 'CAC'], 'I': ['AUU', 'AUC', 'AUA'], 
    'K': ['AAA', 'AAG'], 'L': ['CUU', 'CUC', 'CUA', 'CUG', 'UUA', 'UUG'], 'M': ['AUG'], 'N': ['AAU', 'AAC'], 
    'P': ['CCU', 'CCC', 'CCA', 'CCG'], 'Q': ['CAA', 'CAG'], 'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], '*': ['UAA', 'UAG', 'UGA'], 'T': ['ACU', 'ACC', 'ACA', 'ACG'], 
    'V': ['GUU', 'GUC', 'GUA', 'GUG'], 'W': ['UGG'], 'Y': ['UAU', 'UAC']
}

def list_to_str(og_list):
    return_str = ''
    for item in og_list:
        return_str += str(item) + ' '
    
    return(return_str)