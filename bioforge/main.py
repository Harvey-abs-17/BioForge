import argparse


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

    print(f"Input: {args.input}")
    print(f"Output: {args.out}")
    print(f"Minimum Length: {args.min_length}")

    weight = int(args.min_weight) if args.min_weight.is_integer(
    ) else args.min_weight
    print(f"Minimum Weight: {weight}")


if __name__ == '__main__':
    main()
