# Base class for all BioForge errors.
class BioForgeError(Exception):
    pass


# Raised when a FASTA file has an invalid structure.
class FastaFormatError(BioForgeError):
    pass


# Raised when a DNA sequence contains invalid characters.
class InvalidSequenceError(BioForgeError):
    pass


# Raised when a data file is missing or malformed.
class DataFileError(BioForgeError):
    pass