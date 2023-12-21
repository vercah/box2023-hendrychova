from maw.utils import ALPHABET, to_canonical, reverse_complement

def k_substrings(seq: str, k: int) -> set[str]:
    """Returns the substrings of length k in the given sequence."""
    subs = set()
    for i in range(len(seq)-k+1):
        subs.add(seq[i:i+k])
    return subs

def all_substrings(seq: str, mini: int, maxi: int) -> set[str]:
    """Returns all substring of seq of length in range [mini, maxi]."""
    subs = set()
    for k in range(mini, maxi+1):
        subs.update(k_substrings(seq, k))
    return subs

def add_reverse_complements(seqs: set[str]) -> set[str]:
    """Adds to a given set of strings with their reverse complements."""
    new_seqs = set()
    for seq in seqs:
        new_seqs.add(seq)
        new_seqs.add(reverse_complement(seq))
    return new_seqs


def get_proper_prefixes(seq: str) -> set[str]:
    return set(seq[:i] for i in range(1,len(seq)))

def get_proper_suffixes(seq: str) -> set[str]:
    return set(seq[i:] for i in range(1, len(seq)))

def extended_strings(seq: str) -> set[str]:
    """Returns all possible strings of length |seq|+1 that have seq
    as a substring."""
    exts = set()
    for a in ALPHABET:
        exts.add(a + seq)
        exts.add(seq + a)
    return exts

def all_maws_candidates(seq: str, k: int) -> set[str]:
    """Returns all possible absent words candidates of length 3 up to k"""
    candidates = set()
    for w in add_reverse_complements(all_substrings(seq, 2, k-1)):
        candidates.update(extended_strings(w))
    return candidates

def get_all_maws(sequences: set[str], kmax: int) -> set[str]:
    # TODO: found a counter example for which it doesn't work,
    # look into tests
    maws = set()
    for seq in sequences:
        for x in all_maws_candidates(seq, kmax):
            rx = reverse_complement(x)
            pres = get_proper_prefixes(x)
            sufs = get_proper_suffixes(x)
            subs = pres.union(sufs)
            valide_candiate = True
            for sub in subs:
                for other_seq in sequences:
                    if sub not in other_seq:
                        valide_candiate = False
            if not valide_candiate:
                continue
            for other_seq in sequences:
                if x in other_seq or rx in other_seq:
                    valide_candiate = False
            if valide_candiate:
                maws.add(to_canonical(x))
    return maws

def find_maws(sequences: set[str], kmax: int) -> dict[int, set[str]]:
    maws_set = get_all_maws(sequences, kmax)
    maws = {k: set() for k in range(3, kmax+1)}
    for maw in maws_set:
        maws[len(maw)].add(maw)
    return maws