from utils import ALPHABET, to_canonical, reverse_complement
from typing import Collection
from functools import lru_cache


@lru_cache
def k_substrings(seq: str, k: int) -> set[str]:
    """Returns the substrings of length k in the given sequence."""
    subs = set()
    for i in range(len(seq)-k):
        subs.add(seq[i:i+k])
    return subs

def all_substrings(seq: str, mini: int, maxi: int) -> set[str]:
    """Returns all substring of seq of length in range [mini, maxi]."""
    subs = set()
    for k in range(mini, maxi+1):
        subs.update(k_substrings(seq, k))
    return subs

def extended_strings(seq: str) -> set[str]:
    """Returns all possible strings of length |seq|+1 that have seq
    as a substring."""
    exts = set()
    for a in ALPHABET:
        exts.add(a + seq)
        exts.add(seq + a)
    return exts

def k_maws_of_sequence(seq: str, k: int) -> set[str]:
    """Returns all canonical minimum absent words of length k of
    sequence seq."""
    # TODO: doesn't work because it only ensures that substrings
    # of length k-1 are present, and not all from 3 to k-1.
    maws = set()
    for w in k_substrings(seq, k-1):
        for x in extended_strings(w):
            rx = reverse_complement(x)
            if x not in seq and rx not in seq:
                maws.add(to_canonical(x))
    return maws

def maws(sequences: Collection[str], kmax: int) -> dict[int, list[str]]:
    """Returns all minimum absent words (MAWs) of length 3 to kmax of the set
    of sequences. Each list of MAWs is ordered alphabetically and only
    contains canonical words.
    
    Returns: a dictionary `maws` such that `maws[k]` is the ordered list of
    MAWs of length k.
    """
    maws = {k: [] for k in range(3, kmax+1)}
    for seq in sequences:
        for k in maws.keys():
            maws[k].extend(k_maws_of_sequence(seq, k))
    for k, lst in maws.items():
        maws[k] = sorted(lst)
    return maws