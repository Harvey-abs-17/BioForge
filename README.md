# BioForge

BioForge is a Python command-line pipeline for DNA sequence analysis.

## Project Overview

<!-- Add a short explanation of the project and its purpose. -->

## Pipeline Flow

<!-- Show the main processing steps from FASTA input to the final report. -->

## Installation

<!-- Explain how to clone the repository and prepare the project for use. -->

## Usage

<!-- Add the CLI command, required arguments, and one example. -->

## FASTA Input and Data Files

### FASTA Input

<!-- Explain the expected FASTA format and provide a small example. -->

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

<!-- Explain how an ORF RNA sequence is translated into a protein. -->

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
