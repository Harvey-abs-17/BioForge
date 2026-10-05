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
