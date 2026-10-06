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

<!-- Explain the expected FASTA format and provide a small example. -->

### Data Files

<!-- Explain codon_table.txt and amino_weights.txt. -->

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

<!-- Explain how protein molecular weight is calculated. -->

### Protein Filters

<!-- Explain LengthFilter and WeightFilter. -->

## Output Files

<!-- Explain the report and log files created for each run. -->

## Project Structure

<!-- Add a short tree showing the important project files and folders. -->

## Team Members

<!-- Add the team members and their main responsibilities. -->
