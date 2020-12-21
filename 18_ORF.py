## Problem 18 - ORF (Open Reading Frames)
## Willma
## 12/21/2020

## http://rosalind.info/problems/orf/

import resources

def dna2protein(dnaSeq):
    '''Given a dnaSeq, output corresponding aa chain.

    Input: str of dnaSeq with len%3=0
    dict, codonTableD with keys=codon and vals=aa
    Output: str of amino acid sequence
    '''
    #setup variables
    aaSequence = ''
    i=0
    while i < (len(dnaSeq)-2):
        #more setup
        x=0
        threeLetterDNA = str()

        #set threeLetterDNA to three letters
        while x<3:
            threeLetterDNA += dnaSeq[i]
            i += 1
            x += 1
        
        #find the corresponding aa for the 3 letters and add to aaSequence
        aaSequence += resources.codonDict[threeLetterDNA.replace('T','U')]
    return(aaSequence)

def ReverseSeq(dnaSeq):
    '''
    Finds the corresponding DNA seq and reverses it to prepare
    to be read in 5' to 3'

    Input: DNA sequence
    Output: reversed DNA sequence
    '''
    #corresponding nucelotide dictionary
    corrBpDic = {"C":"G", "G":"C", "A":"T", "T":"A"}

    swappedSeq = str()
    seqIndex = 0
    while(seqIndex < len(dnaSeq)):
        #get corresponding nucleotides
        tempBp = corrBpDic[dnaSeq[seqIndex]]

        #set bp to corresponding bp
        swappedSeq += tempBp

        seqIndex += 1
    
    #reverse string
    reverseIndex = len(swappedSeq)
    reversedSeq = str()
    while reverseIndex > 0:
        tempBp = swappedSeq[reverseIndex - 1]
        reversedSeq += tempBp
        reverseIndex -= 1

    #return reversedSeq
    return(reversedSeq)

def seqORF(dnaSeq):
    '''
    Finds all ORFs in a window of DNA

    Input: DNA sequence 
    Output: list of ORFs in window
    '''
    orfList = list()
    aaSeq = dna2protein(dnaSeq)

    #find start and stop codons
    seqEnd = False
    startLoc = -1
    endLoc = 0
    while seqEnd == False:
        #find start and stop codon locations
        startLoc = aaSeq.find("M", startLoc + 1, len(aaSeq))
        endLoc = aaSeq.find("*", startLoc, len(aaSeq))
        
        #add to orf list
        if (startLoc == -1) or (endLoc == -1):
            #end finding
            seqEnd = True
            break
        else:
            #add orf to list
            tempORF = aaSeq[startLoc:endLoc]
            orfList.append(tempORF)
    
    return(orfList)

def ORF(dnaSeq):
    '''
    Find all ORFs for given dnaSeq.

    Input dnaSeq: str of dnaSeq
    Output: list of strs (all unique orfs translated to aa seq)
    '''

    orfList = list()

    window = 0
    #for each windows forward
    while window < 3:
        for orf in seqORF(dnaSeq[window:]):
            orfList.append(orf)
        window += 1

    #get the reversed dna seq
    reversedSeq = ReverseSeq(dnaSeq)

    window = 0
    #for each window backwards
    while window < 3:
        for orf in seqORF(reversedSeq[window:]):
            orfList.append(orf)
        window += 1

    #remove duplicates
    for orf in orfList:
        if orfList.count(orf) > 1:
            orfList.remove(orf)

    output_path = 'outputs/orf.txt'
    resources.write_file(output_path, (sorted(orfList)))


if __name__ == "__main__":
    file_path = 'datasets/rosalind_orf.txt'
    dna_dict = resources.read_fasta(file_path)
    dna_seq = [seq for seq in dna_dict.values()][0]
    ORF(dna_seq)