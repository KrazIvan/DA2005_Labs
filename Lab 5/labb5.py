# Lab 5. Object-oriented programming. DA2005 Programming techniques HT22. Stockholm University.

class DnaSeq:
    def __init__(self, accession, seq):
        if (seq == "" or seq == None) or (accession == "" or accession == None):
            raise ValueError # Raise a ValueError if the object's seq or accession are empty.
        self.accession = accession
        self.seq = seq
        

    def __len__(self):
        return len(self.seq)

    def __str__(self):
        return f"<DnaSeq accession='{self.accession}'>"


def read_dna(filename):
    '''
    Function for creating a list of DnaSeq objects representing the sequences in a fa file.

    Parameter: Filename of a fa file.

    Output: Returns a list with DnaSeq objects taken from the fa file.

    WARNING: This function uses walrus operators, which don't exist in versions of Python older than 3.8. 
    Make sure you're using an up-to-date version.

    Second WARNING: Only works with fa files that can be interpreted (that have a seq line followed by an accession line, 
    followed by another seq line and so on. All empty lines do get ignored though).

    '''
    dna_list = []

    with open(filename,"r") as file:
        while seq_line := file.readline(): # Reads every line of the file until the end of the file is reached.
            seq_line = seq_line.replace("\n","").replace(">","") # Rids the data of unnecessary characters.
            if not seq_line: # Skips empty lines.
                continue
            # After finding the seq line, the next while loop looks for an accession line. Empty lines are skipped until a valid accession line is found.
            while accession_line := file.readline():
                accession_line = accession_line.replace("\n","")
                if accession_line: # Breaks out of this while loop when the accession line is found, goes back to the first while loop.
                    break

            dna_list.append(DnaSeq(seq_line, accession_line))
    
    return dna_list


def check_exact_overlap(dna_seq1, dna_seq2, min_leng_limit = 10):
    """
    Function for detecting the size of the biggest overlap (greater than a minimum length) between the sequence of a 
    DnaSeq object's suffix with another sequence of a DnaSeq object's prefix.
    
    Mandatory parameters: Two DnaSeq objects (dna_seq1, dna_seq2). 
    Optional parameter: An int as a limit on the smallest overlap size that will be returned (default length limit is 10 unless given a different length limit).

    Output: Returns int of the size of the biggest overlap (greater than a minimum length) between the sequence of a 
    DnaSeq object's suffix with another sequence of a DnaSeq object's prefix. 
    Returns 0 if no overlap is found or if no overlap >= the length limit is found.
    
    """
    overlap_size = 0
    for n in range(len(dna_seq1)):
        if dna_seq1.seq[-n:] == dna_seq2.seq[:n]:
            overlap_size = n # Updates the size for matching characters of a sequence's prefix and another sequence's suffix, that are found.
    if (overlap_size < min_leng_limit):
            return 0 # Returns zero if the biggest overlap found is smaller than the minimum length limit.
    return overlap_size


def overlaps(lst, overlap_func):
    """
    Function for finding the indivudual lengths of the overlaps between DNA sequences and listing them in a dictionary.
    
    Parameters: A list of DnaSeq objects (lst). An overlap function (function that returns the size of the overlaps between DNA sequences as an int).
    
    Output: Returns a dictionary of dictionaries containing the lengths of the overlaps between the DNA sequences and the accessions of the DnaSeq objects.

    """
    overlap_dict = {}
    temp_dict = {}
    for dna_seq1 in lst: # Goes through the data list (the list of DnaSeq objects).
        temp_dict[dna_seq1.accession] = {} # Adds the accession of a DnaSeq object as a key.
        for dna_seq2 in lst: # Goes through the data list again.
            if not dna_seq1 == dna_seq2: # Skips applying the overlap function to the same DnaSeq object.
                overlap_size = overlap_func(dna_seq1, dna_seq2)
                if overlap_size > 0: # Skips adding the entry to the dictionary if no overlaps or no overlaps >= the length limit of overlap_func are found.
                    temp_dict[dna_seq1.accession][dna_seq2.accession] = overlap_size
    for dna_seq1 in temp_dict: # Puts all the non-empty entries of the temporary dictionary into the main dictionary.
        if temp_dict[dna_seq1]:
            overlap_dict[dna_seq1] = temp_dict[dna_seq1]
    return overlap_dict

#
# Testing code. You should not change any code below here. To run the tests
# uncomment the last line in the file.
#
def test_class_DnaSeq():
    s1 = DnaSeq('s1', 'ACGT')
    s2 = DnaSeq('s2', 'ATGTTTGTTTTTCTTGTTTTATTGCCACTAGTCTCTAGTCAGTGTGTTAATCTTACAACCAGAACTCAAT')
    assert len(s1) == 4, 'Your length method (__len__) is not correct.'
    assert len(s2) == 70, 'Your length method (__len__) is not correct.'

    assert str(s1) == "<DnaSeq accession='s1'>", 'The __str__ method is not following the specification.'
    assert str(s2) == "<DnaSeq accession='s2'>", 'The __str__ method is not following the specification.'

    # The rest of this function is verifying that we are indeed raising an exception.
    status = 0
    try:
        s3 = DnaSeq('', 'ACGT')
    except ValueError:
        status += 1
    try:
        s3 = DnaSeq('s3', None)
    except ValueError:
        status += 1

    try:
        s3 = DnaSeq(None, '')
    except ValueError:
        status += 1
    if status != 3:
        raise Exception('class DnaSeq does not raise a ValueError '
                        'exception with initialised with empty '
                        'accession and sequence.')
    print('DnaSeq passed')


def test_reading():
    dna1 = read_dna('ex1.fa')
    assert len(dna1) == 6, 'The file "ex1.fa" has exactly 6 sequences, but your code does not return that.'
    assert list(map(lambda x: x.accession, dna1)) == [f's{i}' for i in range(6)], 'The accessions are not read correctly'

    dna2 = read_dna('ex2.fa')
    assert len(dna2) == 6, 'The file "ex2.fa" has exactly 6 sequences, but your code does not return that.'

    covid = read_dna('sars_cov_2.fa')
    assert len(covid[0].seq) == 29903, 'The length of the genome in "sars_cov_2.fa" is 29903, but your code does not return that.'

    print('read_dna passed')


def test_overlap():
   s0 = DnaSeq('s0', 'AAACCC')
   s1 = DnaSeq('s1', 'CCCGGG')
   s2 = DnaSeq('s2', 'TTTTCC')
   s3 = DnaSeq('s3', 'CCAGGG')
   s4 = DnaSeq('s4', 'GGGGGGGGAAAGGGGG')
   s5 = DnaSeq('s5', 'AAATTTTTTTTTTTTTTTTTTT')

   data1 = [s0, s1, s2, s3]
   assert check_exact_overlap(s0, s1, 2) == 3
   assert check_exact_overlap(s0, s1) == 0
   assert check_exact_overlap(s0, s3, 2) == 2
   assert check_exact_overlap(s1, s2, 2) == 0
   assert check_exact_overlap(s2, s1, 2) == 2
   assert check_exact_overlap(s2, s3, 2) == 2
   assert check_exact_overlap(s4, s5, 1) == 0, 'Do not allow "internal" substrings to overlap. s4 and s5 does not have an overlap.'
   assert check_exact_overlap(s4, s5, 2) == 0
   assert check_exact_overlap(s4, s5, 3) == 0

   res0 = overlaps(data1, lambda s1, s2: check_exact_overlap(s1, s2, 2))
   assert len(res0) == 2, 'You get the wrong number of overlaps'
   assert res0 == {'s0': {'s1': 3, 's3': 2}, 's2': {'s1': 2, 's3': 2}}

   dna_data = read_dna('ex1.fa')
   res1 = overlaps(dna_data, check_exact_overlap)
   assert len(res1) == 5
   for left, right in [('s0', 's1'), ('s1', 's2'), ('s2', 's3'), ('s3', 's4'),
                       ('s4', 's5')]:
       assert res1[left][right], f'Missing overlap of {left} and {right} (in that order)'
   print('overlap code passed')



def test_all():
    test_class_DnaSeq()
    test_reading()
    test_overlap()
    print('Yay, all good')

# Uncomment this to test everything:
# test_all()