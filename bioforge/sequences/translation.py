def translate(rna, codon_table):
    protein = []

    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i+3]
        amino_acid = codon_table.get(codon)

        if amino_acid == "*":
            break

        if amino_acid:
            protein.append(amino_acid)

    return "".join(protein)


sample_codon_table = {
    "AUG": "M",
    "CUU": "L",
    "UCA": "S",
    "GCU": "A",
    "AAA": "K",
    "CCU": "P",
    "UAA": "*",
    "UAG": "*",
    "UGA": "*"
}

rna_complete = "AUGCUUUCAUAG"

print(f"Complete ORF: {translate(rna_complete, sample_codon_table)}")

rna_stop = "AUGGCUAAAUGACCU"

print(f"Stop Translation: {translate(rna_stop, sample_codon_table)}")

rna_incomplete = "AUGCUUUCA"

print(f"Incomplete ORF: {translate(rna_incomplete, sample_codon_table)}")
