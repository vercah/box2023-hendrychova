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

def extended_left(seq: str) -> set[str]:
    """Returns all possible strings of length |seq|+1 that have seq
    as a suffix."""
    exts = set()
    for a in ALPHABET:
        exts.add(a + seq)
    return exts

def extended_right(seq: str) -> set[str]:
    """Returns all possible strings of length |seq|+1 that have seq
    as a prefix."""
    exts = set()
    for a in ALPHABET:
        exts.add(seq + a)
    return exts

def left_maw_candidates(seq: str, k: int) -> set[str]:
    """Returns all possible absent words candidates of length 3 up to k that were created as a left extension"""
    candidates = set()
    for w in add_reverse_complements(all_substrings(seq, 2, k-1)):
        candidates.update(extended_left(w))
    return candidates

def right_maw_candidates(seq: str, k: int) -> set[str]:
    """Returns all possible absent words candidates of length 3 up to k that were created as a right extension"""
    candidates = set()
    for w in add_reverse_complements(all_substrings(seq, 2, k-1)):
        candidates.update(extended_right(w))
    return candidates

def get_all_maws(sequences: set[str], kmax: int) -> set[str]:
    maws = set()
    for seq in sequences:
        left_candidates = left_maw_candidates(seq, kmax)
        right_candidates = right_maw_candidates(seq, kmax)
        all_candidates = left_candidates.union(right_candidates)
        for x in sorted(all_candidates):
            if x in left_candidates:
                necessary = x[0:len(x)-1]
            if x in right_candidates:
                necessary = x[1:len(x)]
            valide_candiate = False
            for other_seq in sequences:
                if necessary in other_seq or reverse_complement(necessary) in other_seq:
                    valide_candiate = True
                    break
            if not valide_candiate:
                continue
            for other_seq in sequences:
                if x in other_seq or reverse_complement(x) in other_seq:
                    valide_candiate = False
                    break
            if valide_candiate:
                maws.add(to_canonical(x))
    return maws

def find_maws(sequences: set[str], kmax: int) -> dict[int, set[str]]:
    maws_set = get_all_maws(sequences, kmax)
    maws = {k: set() for k in range(3, kmax+1)}
    for maw in maws_set:
        maws[len(maw)].add(maw)
    return maws
