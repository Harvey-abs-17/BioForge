class ORF:
    def __init__(self, rna, strand, frame, start_pos, is_complete):
        self.id = None
        self.rna = rna
        self.protein = ""
        self.strand = strand
        self.frame = frame
        self.start_pos = start_pos
        self.is_complete = is_complete
