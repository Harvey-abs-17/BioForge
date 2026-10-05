from abc import ABC, abstractmethod
from bioforge.protein.calculate_weight import calculate_weight

class ProteinFilter(ABC):
    @abstractmethod
    def apply(self, proteins):
        pass

class LengthFilter(ProteinFilter):
    def __init__(self, min_length):
        self.min_length = min_length

    def apply(self, proteins):
        result = []
        for protein in proteins:
            sequence = protein.protein if hasattr(protein, "protein") else protein
            if len(sequence) >= self.min_length:
                result.append(protein)
        return result

class WeightFilter(ProteinFilter):
    def __init__(self, min_weight, amino_weights):
        self.min_weight = min_weight
        self.amino_weights = amino_weights

    def apply(self, proteins):
        result = []
        for protein in proteins:
            sequence = protein.protein if hasattr(protein, "protein") else protein
            protein_weight = calculate_weight(sequence, self.amino_weights)
            if protein_weight >= self.min_weight:
                result.append(protein)
        return result
