import sys
from xopen import xopen
from functools import lru_cache
from readfa import readfq

NUCLEOTIDE_COMPLEMENT = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

def reverse_complement(seq: str) -> str:
    rev = []
    for char in reversed(seq):
        rev.append(NUCLEOTIDE_COMPLEMENT[char])
    return "".join(rev)

@lru_cache
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