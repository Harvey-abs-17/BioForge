این کد رو بزنید 
import logging

from bioforge.errors import InvalidSequenceError
from bioforge.files.fasta import parse_fasta
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