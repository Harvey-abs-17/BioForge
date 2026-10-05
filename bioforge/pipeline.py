import logging
import os
from datetime import datetime

from bioforge.errors import FastaFormatError, InvalidSequenceError
from bioforge.files.data_loader import load_amino_weights, load_codon_table
from bioforge.files.fasta import FastaParser
from bioforge.files.logger import setup_logger
from bioforge.files.reporting import annotate_orfs, write_report
from bioforge.orf.orf_detector import ORFDetector
from bioforge.protein.processing import translate_and_filter
from bioforge.protein.protein_filters import LengthFilter, WeightFilter
from bioforge.sequences.dna import DNASequence
from bioforge.sequences.translation import translate


logger = logging.getLogger("bioforge")


def parse_fasta(path):
    if not os.path.exists(path):
        error = f"FASTA file not found: {path}"
        logger.error(error)
        raise FastaFormatError(error)

    parser = FastaParser(path)
    try:
        return parser.parse()
    except FastaFormatError as error:
        logger.error(str(error))
        raise


def find_all_orfs(fasta_path):
    records = parse_fasta(fasta_path)
    detector = ORFDetector()
    all_orfs = []

    for record in records:
        try:
            dna = DNASequence(record["sequence"])
        except InvalidSequenceError:
            logger.error(f"Record {record['id']} contains an invalid DNA sequence")
            continue

        forward_rna = dna.to_rna()
        reverse_dna = DNASequence(dna.reverse_complement())
        reverse_rna = reverse_dna.to_rna()

        forward_orfs = detector.find_forward_orfs(forward_rna)
        reverse_orfs = detector.find_reverse_orfs(dna.sequence, reverse_rna)

        all_orfs.extend(forward_orfs)
        all_orfs.extend(reverse_orfs)

    return all_orfs


def run_pipeline(
    fasta_path,
    output_directory,
    min_length,
    min_weight,
    codon_table_path="data/codon_table.txt",
    amino_weights_path="data/amino_weights.txt",
):
    os.makedirs(output_directory, exist_ok=True)
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    log_name = f"bioforge_{run_id}.log"
    setup_logger(os.path.join(output_directory, log_name))

    codon_table = load_codon_table(codon_table_path)
    amino_weights = load_amino_weights(amino_weights_path)
    all_orfs = find_all_orfs(fasta_path)

    rna_sequences = []
    for orf in all_orfs:
        rna_sequences.append(orf.rna)

    filters = [
        LengthFilter(min_length),
        WeightFilter(min_weight, amino_weights),
    ]

    filtered_proteins = translate_and_filter(
        rna_sequences,
        codon_table,
        filters,
    )

    filtered_orfs = []
    for orf in all_orfs:
        orf.protein = translate(orf.rna, codon_table)
        if orf.protein in filtered_proteins:
            filtered_orfs.append(orf)

    annotate_orfs(filtered_orfs)
    write_report(filtered_orfs, output_directory, run_id)
    return filtered_orfs
