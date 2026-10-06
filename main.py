import argparse

from bioforge.pipeline import run_pipeline


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--input', required=True, type=str,
                        help='Path to the input FASTA file.')
    parser.add_argument('--out', required=True, type=str,
                        help='Path to the output directory.')
    parser.add_argument('--min-length', required=True,
                        type=int, help='Minimum accepted protein length.')
    parser.add_argument('--min-weight', required=True, type=float,
                        help='Minimum accepted protein molecular weight.')

    args = parser.parse_args()

    run_pipeline(
        fasta_path=args.input,
        output_directory=args.out,
        min_length=args.min_length,
        min_weight=args.min_weight,
    )


if __name__ == '__main__':
    main()
