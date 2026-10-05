import logging
import os

from bioforge.errors import InvalidSequenceError
from bioforge.files.data_loader import load_amino_weights, load_codon_table
from bioforge.files.fasta import parse_fasta
from bioforge.files.logger import setup_logger
from bioforge.files.reporting import annotate_orfs, write_report
from bioforge.orf.orf_detector import ORFDetector
from bioforge.protein.processing import translate_orfs
from bioforge.protein.protein_filters import LengthFilter, WeightFilter
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


def run_pipeline(
    fasta_path,
    output_directory,
    min_length,
    min_weight,
    codon_table_path="data/codon_table.txt",
    amino_weights_path="data/amino_weights.txt",
):
    os.makedirs(output_directory, exist_ok=True)
    setup_logger(os.path.join(output_directory, "bioforge.log"))

    codon_table = load_codon_table(codon_table_path)
    amino_weights = load_amino_weights(amino_weights_path)
    records = load_records_with_orfs(fasta_path)

    orfs = []
    for record in records:
        record_orfs = record["orfs"]
        translate_orfs(record_orfs, codon_table)
        orfs.extend(record_orfs)

    filters = [
        LengthFilter(min_length),
        WeightFilter(min_weight, amino_weights),
    ]

    filtered_orfs = orfs
    for protein_filter in filters:
        filtered_orfs = protein_filter.apply(filtered_orfs)

    annotate_orfs(filtered_orfs)
    write_report(filtered_orfs, output_directory)
    return filtered_orfs
