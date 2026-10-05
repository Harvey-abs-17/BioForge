from bioforge.sequences.translation import translate


def translate_sequences(rna_sequences, codon_table):
    proteins = []
    for rna in rna_sequences:
        protein = translate(rna, codon_table)
        proteins.append(protein)
    return proteins


def filter_proteins(proteins, filters):
    filtered_proteins = proteins
    for protein_filter in filters:
        filtered_proteins = protein_filter.apply(filtered_proteins)
    return filtered_proteins


def translate_and_filter(rna_sequences, codon_table, filters):
    proteins = translate_sequences(rna_sequences, codon_table)
    return filter_proteins(proteins, filters)
