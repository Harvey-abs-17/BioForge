from bioforge.sequences.translation import translate
from bioforge.protein.protein_filters import *

def translate_and_filter(rna_sequences, codon_table, filters):
    proteins = []
    for rna in rna_sequences:
        protein = translate(rna, codon_table)
        proteins.append(protein)

    filtered_proteins = proteins
    for protein_filter in filters:
        filtered_proteins = protein_filter.apply(filtered_proteins)

    return filtered_proteins
