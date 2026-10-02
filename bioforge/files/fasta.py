import logging
import re


from bioforge.errors import FastaFormatError

logger = logging.getLogger(__name__)

# regex from the project document
HEADER_PATTERN = r"^>\s*(?P<id>\S+)\s*(?P<desc>.*)$"


def parse_header(line, line_number):
    """Split a header line into id and description."""
    match = re.match(HEADER_PATTERN, line)
    if match is None:
        raise FastaFormatError(f"Line {line_number}: header has no ID")
    header_id = match.group("id")
    description = match.group("desc")
    return header_id, description


def extract_organism(description):
    """Return the organism name from the description, or None."""
    words = description.split()
    for word in words:
        if word.startswith("organism="):
            return word[len("organism="):]
    return None


def build_record(header_id, description, sequence_lines, line_number):
    """Make a record dictionary from a header and its sequence lines."""
    if len(sequence_lines) == 0:
        raise FastaFormatError(
            f"Line {line_number}: header {header_id} has no sequence"
        )
    sequence = "".join(sequence_lines)
    organism = extract_organism(description)
    record = {
        "id": header_id,
        "description": description,
        "sequence": sequence,
        "organism": organism,
    }
    return record
def parse_fasta(path):
    """Read a FASTA file and return a list of record dictionaries."""
    records = []
    seen_ids = []

    # information about the record we are reading right now
    current_id = None
    current_description = ""
    current_lines = []
    current_line_number = 0

    with open(path, encoding="utf-8") as file:
        line_number = 0
        for line in file:
            line_number = line_number + 1
            line = line.strip()

            # skip empty lines
            if line == "":
                continue

            if line.startswith(">"):
                # save the previous record before starting a new one
                if current_id is not None:
                    record = build_record(current_id, current_description,
                                          current_lines, current_line_number)
                    records.append(record)

                header_id, description = parse_header(line, line_number)

                if header_id in seen_ids:
                    logger.warning(f"Line {line_number}: duplicate ID {header_id}")
                seen_ids.append(header_id)

                # start the new record
                current_id = header_id
                current_description = description
                current_lines = []
                current_line_number = line_number
            else:
                if current_id is None:
                    raise FastaFormatError(
                        f"Line {line_number}: sequence before the first header"
                    )
                current_lines.append(line.upper())

    # the last record has no ">" after it, so save it here
    if current_id is not None:
        record = build_record(current_id, current_description,
                              current_lines, current_line_number)
        records.append(record)

    if len(records) == 0:
        raise FastaFormatError("The FASTA file is empty")

    return records