import logging
import re

from bioforge.errors import FastaFormatError

logger = logging.getLogger("bioforge")


HEADER_PATTERN = r"^>\s*(?P<id>\S+)\s*(?P<desc>.*)$"


class FastaParser:
    """Read a FASTA file and turn it into a list of record dictionaries."""

    def __init__(self, path):
        self.path = path
        self._reset()

    def parse(self):
        """Read the file and return a list of record dictionaries."""
        self._reset()

        with open(self.path, encoding="utf-8") as file:
            line_number = 0
            for line in file:
                line_number = line_number + 1
                line = line.strip()

                
                if line == "":
                    continue

                if line.startswith(">"):
                    self._start_new_record(line, line_number)
                else:
                    self._add_sequence_line(line, line_number)

        
        self._save_current_record()

        if len(self.records) == 0:
            raise FastaFormatError("The FASTA file is empty")

        return self.records

    def _reset(self):
        """Clear everything before a new read."""
        self.records = []
        self.seen_ids = []
        self.current_id = None
        self.current_description = ""
        self.current_lines = []
        self.current_line_number = 0

    def _start_new_record(self, line, line_number):
        """Save the previous record and start a new one from a header line."""
        self._save_current_record()

        header_id, description = self._parse_header(line, line_number)

        if header_id in self.seen_ids:
            logger.warning(f"Duplicate sequence ID: {header_id}")
        self.seen_ids.append(header_id)

        self.current_id = header_id
        self.current_description = description
        self.current_lines = []
        self.current_line_number = line_number

    def _add_sequence_line(self, line, line_number):
        """Add one DNA line to the current record."""
        if self.current_id is None:
            raise FastaFormatError(
                f"Line {line_number}: sequence before the first header"
            )
        self.current_lines.append(line.upper())

    def _save_current_record(self):
        """Turn the current record into a dictionary and keep it."""
        if self.current_id is None:
            return

        if len(self.current_lines) == 0:
            raise FastaFormatError(
                f"Line {self.current_line_number}: "
                f"header {self.current_id} has no sequence"
            )

        record = {
            "id": self.current_id,
            "description": self.current_description,
            "sequence": "".join(self.current_lines),
            "organism": self._extract_organism(self.current_description),
        }
        self.records.append(record)

    def _parse_header(self, line, line_number):
        """Split a header line into id and description."""
        match = re.match(HEADER_PATTERN, line)
        if match is None:
            raise FastaFormatError(f"Line {line_number}: header has no ID")
        return match.group("id"), match.group("desc")

    def _extract_organism(self, description):
        """Return the organism name from the description, or None."""
        words = description.split()
        for word in words:
            if word.startswith("organism="):
                return word[len("organism="):]
        return None


def parse_fasta(path):
    """Read a FASTA file and return a list of record dictionaries."""
    parser = FastaParser(path)
    return parser.parse()