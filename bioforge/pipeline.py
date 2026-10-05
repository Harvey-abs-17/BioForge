import logging

from bioforge.errors import InvalidSequenceError
from bioforge.files.fasta import parse_fasta
from bioforge.orf.orf_detector import ORFDetector
from bioforge.sequences.dna import DNASequence


logger = logging.getLogger("bioforge")


def load_valid_records(fasta_path):
    records = parse_fasta(fasta_path)
    valid_records = []

    for record in records:
        try:
            DNASequence(record["sequence"])
            valid_records.append(record)

        except InvalidSequenceError:
            logger.error(
                "Record %s contains an invalid DNA sequence",
                record["id"],
            )

    return valid_records


def load_records_with_orfs(fasta_path):
    records = load_valid_records(fasta_path)
    detector = ORFDetector()
    records_with_orfs = []

    for record in records:
        dna = DNASequence(record["sequence"])
        forward_rna = dna.to_rna()

        reverse_dna = DNASequence(dna.reverse_complement())
        reverse_rna = reverse_dna.to_rna()

        forward_orfs = detector.find_forward_orfs(forward_rna)
        reverse_orfs = detector.find_reverse_orfs(
            dna.sequence,
            reverse_rna,
        )

        record_with_orfs = record.copy()
        record_with_orfs["orfs"] = forward_orfs + reverse_orfs
        records_with_orfs.append(record_with_orfs)

    return records_with_orfs
