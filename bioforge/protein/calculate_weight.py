def calculate_weight(protein, amino_weights):
    total = 0
    for amino_acid in protein:
        total += amino_weights[amino_acid]
    return total
