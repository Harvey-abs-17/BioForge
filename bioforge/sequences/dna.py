class DNASequence:
    def __init__(self, sequence):
        self.sequence = sequence.upper()
        self.validate()

    def validate(self):
        for char in self.sequence:
            if char not in ['A', 'T', 'C', 'G']:
                raise InvalidSequenceError("Invalid DNA sequence")

    def complement(self):
        comp_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        result = ""
        for char in self.sequence:
            result += comp_dict[char]
        return result

    def reverse_complement(self):
        comp = self.complement()
        return comp[::-1]

    def to_rna(self):
        return self.sequence.replace("T", "U")

    def gc_content(self):
        length = len(self.sequence)
        if length == 0:
            return 0.0
        
        g_count = self.sequence.count('G')
        c_count = self.sequence.count('C')
        return ((g_count + c_count) / length) * 100