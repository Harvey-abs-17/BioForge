class ORF:
    def __init__(self, protein, strand, frame, start_pos, is_complete):
        self.protein = protein
        self.strand = strand
        self.frame = frame
        self.start_pos = start_pos
        self.is_complete = is_complete
