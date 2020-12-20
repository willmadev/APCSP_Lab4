## Problem 16 - MPRT (Finding a Protein Motif)
## Willma
## 12/21/2020

## http://rosalind.info/problems/mprt/

import resources

def MPRT(id_list):
    '''
    Finds locations of the N-glycosylation motif \n
    Input: List of Uniprot IDs \n
    Output: Writes ID followed by list of locations to outputs/mprt.txt
    '''
    # get fasta file from uniprot
    output_list = []
    fasta_dict = dict()
    for prot_id in id_list:
        fasta_dict.update(resources.get_uniprot(prot_id))
        protein = fasta_dict[prot_id]

        # find locations of motif
        locations = []
        i = 0
        while i < len(protein) - 2:
            #if i is start of motif
            if (protein[i] == 'N' and \
                protein[i+1] != 'P' and \
                (protein[i+2] == 'S' or protein[i+2] == 'T') and \
                protein[i+3] != 'P'):
                locations.append(i + 1)

            i+=1

        #only append if there are motifs
        if locations != []:
            output_list.append(prot_id)
            output_list.append(resources.list_to_str(locations))

    # write to file
    output_path = 'outputs/mprt.txt'
    resources.write_file(output_path, output_list)

if __name__ == "__main__":
    file_path = 'datasets/rosalind_mprt.txt'
    id_list = [data for data in resources.read_file(file_path).split('\n')]
    MPRT(id_list)