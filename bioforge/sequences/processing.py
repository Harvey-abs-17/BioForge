import logging

from bioforge.errors import InvalidSequenceError
from bioforge.files.fasta import parse_fasta
from bioforge.sequences.dna import DNASequence

logger = logging.getLogger("bioforge")


def load_dna_records(path):
    """Read a FASTA file and return the records that have valid DNA."""
    fasta_records = parse_fasta(path)
    valid_records = []

    for record in fasta_records:
        try:
            dna = DNASequence(record["sequence"])
        except InvalidSequenceError:
            logger.warning(f"Invalid DNA sequence: {record['id']}")
            continue

        new_record = record.copy()
        new_record["dna"] = dna
        valid_records.append(new_record)

    return valid_records