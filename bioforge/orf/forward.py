from .models import ORF


def find_forward_orfs(rna_sequence, codon_table):
    orfs = []
    stop_codons = ["UAA", "UAG", "UGA"]

    for frame in range(3):
        position = frame

        while position + 2 < len(rna_sequence):
            codon = rna_sequence[position:position + 3]

            if codon == "AUG":
                protein = ""
                is_complete = False
                current_position = position

                while current_position + 2 < len(rna_sequence):
                    current_codon = rna_sequence[current_position:current_position + 3]

                    if current_codon in stop_codons:
                        is_complete = True
                        break

                    protein = protein + codon_table[current_codon]
                    current_position = current_position + 3

                orf = ORF(
                    protein,
                    "Forward",
                    frame,
                    position,
                    is_complete,
                )

                orfs.append(orf)

            position = position + 3

    return orfs
