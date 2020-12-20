import logging
import requests

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.ERROR, datefmt="%H:%M:%S")

def read_file(file_path):
    '''
    Input: file path \n
    Output: string of data in file
    '''
    with open(file_path) as f:
        file_data = f.read()
    return file_data

def read_fasta(file_path):
    '''
    Input: file path \n
    Output: Dictionary with description as key and DNA sequence as value
    '''
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
    '''
    Input: File Path, List with each item as a new line
    '''
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
    '''
    Input: List \n
    Output: Rosalind List (space separated string)
    '''
    return_str = ''
    for item in og_list:
        return_str += str(item) + ' '
    
    return(return_str)

def status_code_check(response):
    '''
    Input: response
    Output: bool
    '''
    
    if response.status_code == 200:
        return True
    else:
        if response.status_code == 422:
            logging.error("RESPONSE 422 - CHECK MESSAGE")
            logging.error(response.text)
        elif response.status_code == 429:
            logging.error("RESPONSE 429 - Processing too many requests")
            logging.error(response.text)
        elif response.status_code == 500:
            logging.error("RESPONSE 500 - Internal Server Error")
            logging.error(response.text)
        elif response.status_code == 404:
            logging.error("RESPONSE 404")
        else:
            logging.error("Unexpected Error")
            logging.error(response.status_code)
        
        return False

def get_uniprot(uniprot_id):
    '''
    Input: uniprot id \n
    Output: dictionary with uniprot id as key and dna string as value
    '''
    url = 'http://www.uniprot.org/uniprot/' + uniprot_id + '.fasta'
    try:
        # API GET request
        r = requests.get(url)
    except:
        # GET request error
        print('API GET ERROR ------------------')
        print(r.status_code)
    
    # status code error
    if not status_code_check:
        return (Exception)
    
    key = str()
    sequence = str()
    dictionary = dict()

    fasta_text = [line for line in r.text.split('\n')]
    for line in fasta_text:
        #if the line starts with > save the rest of the line as the key
        if line == '':
            continue
        if line[0] == ">":
            #
            if(key != ""):
                dictionary[key] = sequence
                key = str()
                sequence = str()
            # key = line[1:].strip("\n")
            key = uniprot_id
        else:
            sequence = sequence + line.strip("\n")
        #add this line to the existing sequence
        

        #if the file doesn't end with a \n
    if key not in dictionary.keys():
        dictionary[key] = sequence

    return(dictionary)