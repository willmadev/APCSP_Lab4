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