# BioForge

BioForge is a Python command-line pipeline for DNA sequence analysis.

## Project Overview

<!-- Add a short explanation of the project and its purpose. -->

## Pipeline Flow

<!-- Show the main processing steps from FASTA input to the final report. -->

## Installation

<!-- Explain how to clone the repository and prepare the project for use. -->

## Usage

Run BioForge from the project root using:

python main.py --input input/input.fasta --out output --min-length 4 --min-weight 500

All four arguments are required:

- --input: Path to the input FASTA file
- --out: Path to the output directory
- --min-length: Minimum accepted protein length
- --min-weight: Minimum accepted protein molecular weight

Example:

python main.py --input samples/example.fasta --out output --min-length 4 --min-weight 500

BioForge reads the FASTA records, processes their DNA sequences, detects ORFs, translates them into proteins, applies the requested filters, and writes the results into the output directory.

## FASTA Input and Data Files

### FASTA Input

BioForge accepts a multi-record FASTA file as its input.

Each record starts with a header line beginning with `>`. The first part of the header is used as the sequence ID, and the remaining text is stored as the description.

If the header contains an `organism` value, BioForge extracts it separately.

Example:

```text
>seq001 organism=E_coli sample=A
ATGCTTTCATAG

>seq002 organism=Human sample=B
cccatggggtaa
```

For each record, BioForge extracts:

- ID
- Description
- DNA sequence
- Organism, when available

Empty lines are ignored. Lowercase DNA sequences are accepted and converted to uppercase.

A FASTA file is considered invalid when:

- Sequence data appears before the first header.
- A header does not have a sequence.
- The file does not contain any records.

When a duplicate sequence ID is found, a warning is written to the log file.

The FASTA file is opened using UTF-8 encoding.

### Data Files

BioForge reads the codon table and amino acid weights from these files:

data/codon_table.txt
data/amino_weights.txt


The values are loaded from the files when the program runs and are not hardcoded in the Python code.

Each line of codon_table.txt contains an RNA codon and its amino acid code:

AUG M
UUU F
UAA *


The * character represents a stop codon.

Each line of amino_weights.txt contains an amino acid code and its molecular weight:

A 71.037
C 103.009
M 131.040


Empty lines and lines beginning with # are ignored.

Both files are opened using UTF-8 encoding.

A missing file, an empty file, or a malformed line raises DataFileError. The error includes the malformed line number when available and is written to the log file.

## DNA Processing and ORF Detection

### DNA Operations

<!-- Explain DNA validation, RNA conversion, and reverse complement. -->

### ORF Detection

<!-- Explain reading frames, strands, and complete or incomplete ORFs. -->

## Translation and Protein Processing

### RNA Translation

BioForge translates each detected ORF from RNA into a protein sequence.

The RNA sequence is read three characters at a time. Each group of three characters is a codon.

The codon table is loaded from:

data/codon_table.txt

The complete codon table is not hardcoded in the translation code.

Example:

RNA: AUG CUU UCA UAG

Codon translation:

AUG → M
CUU → L
UCA → S
UAG → Stop

The resulting protein is:

MLS

Translation starts from the beginning of the detected ORF and stops when one of these stop codons is found:

UAA
UAG
UGA

The stop codon is not included in the final protein sequence.

If an incomplete ORF does not contain a stop codon, BioForge translates all of its available complete codons.

### Molecular Weight

BioForge calculates the molecular weight of each translated protein.

The amino acid weights are loaded from:

data/amino_weights.txt

The weights are not hardcoded in the protein-processing code.

The molecular weight is calculated by adding the weight of every amino acid in the protein sequence.

Example weights:

M 131.040
A 71.037
C 103.009

Protein:

MAC

Calculation:

M = 131.040
A = 71.037
C = 103.009

Total Weight = 305.086


### Protein Filters

BioForge applies two filters to the translated protein sequences:

- LengthFilter
- WeightFilter

Both filters use the same method:

apply(proteins)

LengthFilter keeps proteins whose sequence length is greater than or equal to the minimum length provided through --min-length.

Example:

Proteins: MA, MAKG, MAKGT
Minimum Length: 4
Result: MAKG, MAKGT

The condition is:

Protein Length >= Minimum Length

WeightFilter keeps proteins whose molecular weight is greater than or equal to the minimum weight provided through --min-weight.

Example:

Protein 1 Weight: 180.0
Protein 2 Weight: 320.0
Protein 3 Weight: 510.0
Minimum Weight: 300.0
Result: Protein 2, Protein 3

The condition is:

Protein Weight >= Minimum Weight

The filters are applied in this order:

LengthFilter
↓
WeightFilter

Each filter returns a new list containing only the matching protein sequences.

## Output Files

<!-- Explain the report and log files created for each run. -->

## Project Structure

<!-- Add a short tree showing the important project files and folders. -->

## Team Members

<!-- Add the team members and their main responsibilities. -->
