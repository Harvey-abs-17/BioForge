from calculate_weight import calculate_weight

def length_filter(proteins, min_length):
        result = []
        for protein in proteins:
            if len(protein) >= min_length:
                result.append(protein)
        return result

def weight_filter(proteins, min_weight, amino_weights):
        result = []
        for protein in proteins:
             protein_weight = calculate_weight(protein, amino_weights)
             if protein_weight >= min_weight:
                 result.append(protein)
        return result