ALPHABET = "ACGT"

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

def to_canonical(seq: str) -> str:
    rev = reverse_complement(seq)
    if rev < seq:
        return rev
    else:
        return seq