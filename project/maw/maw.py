import sys
from xopen import xopen
from maw.readfa import readfq

def read_fa_sequences(file_name: str) -> dict[str, str]:
    sequences = dict()
    for seq_name, seq, _ in readfq(xopen(file_name)):
        if seq_name in sequences:
            raise NameError("Duplicate sequence name.")
        sequences[seq_name] = seq
    return sequences


def main():
    sequences = read_fa_sequences(sys.argv[1])
    for name, seq in sequences.items():
        print(name, len(seq))

if __name__ == "__main__":
    main()