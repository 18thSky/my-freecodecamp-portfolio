def complementary_dna(strand):
    dna_pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}
    new_dna_strand = ""
    for letter in strand:
        new_dna_strand += dna_pairs[letter]
    
    return new_dna_strand
    

complementary_dna("ACGT")
complementary_dna("ATGCGTACGTTAGC")
complementary_dna("GGCTTACGATCGAAG")
complementary_dna("GATCTAGCTAGGCTAGCTAG")