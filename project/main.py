from maw.readfa import read_fa_sequences
import maw.naive as naive
import maw.better as better
import maw.fast as fast
from maw.fmt import to_tsv
from maw.fmt import pprint
import argparse


def main():
    parser = argparse.ArgumentParser(prog="Minimal Absent Words")
    parser.add_argument("-f", "--file", required=True, type=str)
    parser.add_argument("-k", "--kmax", type=int, required=True)
    parser.add_argument("-a", "--algo", choices=["naive", "string-ext", "fast-string-ext"], default="fast-string-ext")
    parser.add_argument("-p", "--print", action="store_true")
    parser.add_argument("-t", "--tsv", default="", type=str)
    parser.add_argument("-s", "--sample", type=int, default=0)

    args = parser.parse_args()

    if args.kmax < 3:
        print("Error: kmax must greater or equal to 3.")
        exit()
    
    
    print(f"Loading {args.file}...", end="", flush=True)
    sequences = read_fa_sequences(args.file)
    print(f" {len(sequences)} sequences loaded.")

    if args.sample > 0:
        sequences = set(list(sequences)[:args.sample])
        print(f"Kept {len(sequences)} sequences.")

    maws: dict[int, set[str]]
    match args.algo:
        case "naive":
            maws = naive.find_maws(sequences, args.kmax)
        case "string-ext":
            maws = better.find_maws(sequences, args.kmax)
        case "fast-string-ext":
            maws = fast.find_maws(sequences, args.kmax)
        case _:
            raise RuntimeError("Invalid algorithm option.")
    
    if args.tsv == "" or args.print:
        pprint(maws)
    if args.tsv != "":
        to_tsv(maws, args.tsv)



if __name__ == "__main__":
    main()