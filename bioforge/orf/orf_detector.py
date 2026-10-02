from .models import ORF


class ORFDetector:
    def __init__(self, codon_table):
        self.codon_table = codon_table

    def find_forward_orfs(self, rna_sequence):
        orfs = []

        for frame in range(3):
            position = frame

            while position + 2 < len(rna_sequence):
                codon = rna_sequence[position:position + 3]

                if codon == "AUG":
                    orf = self.create_orf(rna_sequence, frame, position)
                    orfs.append(orf)

                position = position + 3

        return orfs

    def create_orf(self, rna_sequence, frame, start_position):
        protein = ""
        position = start_position
        stop_codons = ["UAA", "UAG", "UGA"]

        while position + 2 < len(rna_sequence):
            codon = rna_sequence[position:position + 3]

            if codon in stop_codons:
                return ORF(
                    protein=protein,
                    strand="Forward",
                    frame=frame,
                    start_pos=start_position,
                    is_complete=True,
                )

            protein = protein + self.codon_table[codon]
            position = position + 3

        return ORF(
            protein=protein,
            strand="Forward",
            frame=frame,
            start_pos=start_position,
            is_complete=False,
        )

    def find_reverse_orfs(self, original_dna, reverse_rna):
        reverse_orfs = self.find_forward_orfs(reverse_rna)

        for orf in reverse_orfs:
            original_start_pos = len(original_dna) - orf.start_pos - 3

            orf.start_pos = original_start_pos
            orf.strand = "Reverse"

        return reverse_orfs
