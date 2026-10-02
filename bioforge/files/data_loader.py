def load_codon_table(path="data/codon_table.txt"):
    codon_dict = {}
    f = open(path, "r")
    for line in f:
        line = line.strip()
        if line != "":
            parts = line.split()
            codon = parts[0]
            amino = parts[1]
            codon_dict[codon] = amino
    f.close()
    return codon_dict


def load_amino_weights(path="data/amino_weights.txt"):
    weights_dict = {}
    f = open(path, "r")
    for line in f:
        line = line.strip()
        if line != "":
            parts = line.split()
            amino = parts[0]
            weight = float(parts[1])
            weights_dict[amino] = weight
    f.close()
    return weights_dict
