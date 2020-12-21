## Problem 22 - SPLC (RNA Splicing)
## Willma
## 12/21/2020

## http://rosalind.info/problems/splc/

import resources

def SPLC(fasta_dict):
    '''
    Input: Dict with description as key and dna string as value \n
    Output: Protein string resulting from transcribing and translating the exons
    '''
    dna_list = [seq for seq in fasta_dict.values()]
    
    dna_seq = str(dna_list[0])
    substrings = dna_list
    substrings.remove(dna_seq)

    for intron in substrings:
        split_list = dna_seq.split(intron)
        dna_seq = ''
        for split in split_list:
            dna_seq += split

    #dna to protein
    rna = dna_seq.replace('T', 'U')
    
    i=0
    prot = ''
    while i < len(rna):
        window = rna[i:i+3]
        prot += resources.codonDict[window]
        i+=3

    return(prot.strip('*'))

if __name__ == "__main__":
    file_path = 'datasets/rosalind_splc.txt'
    fasta_dict = resources.read_fasta(file_path)
    print(SPLC(fasta_dict))