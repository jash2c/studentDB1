def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1)>len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    n = 0
    for char in dna:
        if nucleotide == char:
            n = n+1

    return n

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna1.find(dna2)>-1


def is_valid_sequence(dna):
    '''
    (str) -> bool
    The function verifies is dna is a valid dna sequence. Returns True if it is, otherwise False.
    
    >>>is_valid_sequence('GACATAC')
    True
    >>>is_valid_sequence('adsa2')
    False
    '''
    n=0
    
   #check if lowercase
    for char in dna:
        if char == 'G' or char == 'C' or char == 'T' or char == 'A':
            n=n+1

    return n == len(dna)
    
                  
def insert_sequence(dna1,dna2,n):
    '''
    (str,str,int)-> str
    Returns a new sequence based off of the 2 dnas and the num is where we insert the sequence.

    >>>insert_sequence('CCGG','AT',2)
    'CCATGG'
    '''
    
    return dna1[:n]+dna2+dna1[n:]

def get_complement(nucleotide):
    '''
    (str) -> str
    Return what other nucleotide/s is complementary to the foregoing.

    >>>get_complement('A')
    'T'
    >>>get_complement('G')
    'C'
    >>>get_complement('C')
    'G'
    '''
    if nucleotide == 'A':
        return 'T'
    if nucleotide == 'T':
        return 'A'
    if nucleotide == 'G':
        return 'C'
    if nucleotide == 'C':
        return 'G'

def get_complementary_sequence(nucleotide):
    '''
    (str) -> str
    returns the nucleotide with its complementary nucleotide

    >>>get_complementary_sequence('C')
    'CG'
    >>>get_complementary_sequence('T')
    'TA'
    '''
    
    newtide =''

    for char in nucleotide:
        if char == 'A':
            newtide = newtide + 'T'
        if char == 'T':
            newtide = newtide + 'A'
        if char == 'G':
            newtide = newtide + 'C'
        if char == 'C':
            newtide = newtide + 'G'

    return newtide

    

    
            
