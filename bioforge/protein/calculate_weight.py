def calculate_weight(protein, amino_weights):
    total = 0
    for amino_acid in protein:
        if amino_acid in amino_weights:
            total += amino_weights.get(amino_acid)
    return total
