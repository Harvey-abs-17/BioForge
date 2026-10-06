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

<!-- Explain codon_table.txt and amino_weights.txt. -->

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
