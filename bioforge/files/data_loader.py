import logging
import os

from bioforge.errors import DataFileError


logger = logging.getLogger("bioforge")


def load_codon_table(path="data/codon_table.txt"):
    lines = _read_data_file(path)
    codon_table = {}

    for line_number, line in lines:
        parts = line.split()
        if len(parts) != 2:
            _data_error(path, line_number, "malformed line")

        codon, amino_acid = parts
        codon_table[codon] = amino_acid

    if len(codon_table) == 0:
        _data_error(path, None, "data file is empty")

    return codon_table


def load_amino_weights(path="data/amino_weights.txt"):
    lines = _read_data_file(path)
    amino_weights = {}

    for line_number, line in lines:
        parts = line.split()
        if len(parts) != 2:
            _data_error(path, line_number, "malformed line")

        amino_acid, weight = parts
        if not weight.replace(".", "", 1).isdigit():
            _data_error(path, line_number, "malformed line")

        amino_weights[amino_acid] = float(weight)

    if len(amino_weights) == 0:
        _data_error(path, None, "data file is empty")

    return amino_weights


def _read_data_file(path):
    if not os.path.exists(path):
        _data_error(path, None, "data file not found")

    lines = []
    with open(path, encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if line != "" and not line.startswith("#"):
                lines.append((line_number, line))
    return lines


def _data_error(path, line_number, message):
    if line_number is None:
        error = f"{path}: {message}"
    else:
        error = f"{path}, line {line_number}: {message}"

    logger.error(error)
    raise DataFileError(error)
