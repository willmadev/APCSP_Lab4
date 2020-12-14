def read_file(file_path):
    '''
    Input: file path \n
    Output: string of data in file
    '''
    with open(file_path) as f:
        file_data = f.read()
    return file_data