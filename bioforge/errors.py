class BioForgeError(Exception):
    """Base class for all BioForge errors."""


class FastaFormatError(BioForgeError):
    """Raised when a FASTA file has an invalid structure."""


class InvalidSequenceError(BioForgeError):
     """Raised when a DNA sequence contains invalid characters."""


class DataFileError(BioForgeError):
     """Raised when a data file is missing or malformed."""
