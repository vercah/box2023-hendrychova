from __future__ import annotations
from maw.karkkainen_sanders import simple_kark_sort
from maw.utils import ALPHABET
from maw.utils import reverse_complement
from maw.utils import to_canonical


class Sequence:
    def __init__(self, seq: str) -> None:
        self._seq = seq
        self.sa = simple_kark_sort(seq)
        self.first_occ = dict()
        self.last_occ = dict()
        for i in range(len(seq)):
            j = len(seq)-i-1
            a, b = seq[self.sa[i]], seq[self.sa[j]]
            if a not in self.first_occ:
                self.first_occ[a] = i
            if b not in self.last_occ:
                self.last_occ[b] = j
    
    def __str__(self) -> str:
        return self._seq
    
    def __len__(self) -> int:
        return len(self._seq)
    
    def __contains__(self, sub: str) -> bool:
        # return sub in self.seq
        if sub[0] not in self.first_occ:
            return False
        a = self.first_occ[sub[0]]
        b = self.last_occ[sub[0]]
        while a <= b:
            m = (a + b)//2
            s = self.sa[m]
            suf = self[s:s+len(sub)]
            if suf == sub:
                return True
            elif sub < suf:
                b = m-1
            else:
                a = m+1
        return False
    
    def __getitem__(self, slice) -> str:
        return self._seq[slice]


def k_substrings(seq: Sequence, k: int) -> set[str]:
    """Returns the substrings of length k in the given sequence."""
    subs = set()
    for i in range(len(seq)-k+1):
        subs.add(seq[i:i+k])
    return subs

def all_substrings(seq: Sequence, mini: int, maxi: int) -> set[str]:
    """Returns all substring of seq of length in range [mini, maxi]."""
    subs = set()
    for k in range(mini, maxi+1):
        subs.update(k_substrings(seq, k))
    return subs

def add_reverse_complements(strs: set[str]) -> set[str]:
    """Adds to a given set of strings with their reverse complements."""
    new_strs = set()
    for s in strs:
        new_strs.add(s)
        new_strs.add(reverse_complement(s))
    return new_strs

def find_maws(sequences: set[str], kmax: int) -> dict[int, set[str]]:
    """Returns all minimum absent words (MAWs) of length 3 to kmax of the set
    of sequences. Each set of MAWs contains only the canonical strings.
    
    Returns: a dictionary `maws` such that `maws[k]` is the set of MAWs
    of length k in the set of sequences.
    """
    maws = {k: set() for k in range(3, kmax+1)}

    seqs: list[Sequence] = []
    for i, s in enumerate(sequences):
        # print(f"Initializing sequence {i}")
        seqs.append(Sequence(s))
    
    rev = reverse_complement

    substrings = set()
    for seq in seqs:
        substrings.update(add_reverse_complements(all_substrings(seq, 2, kmax-1)))
    
    for sub in substrings:
        for a in ALPHABET:
            cand = a + sub
            valid = False
            for seq in seqs:
                w = cand[:-1] 
                if w in substrings or rev(w) in substrings:
                    valid = True
                    break
            if valid:
                for seq in seqs:
                    if cand in seq or rev(cand) in seq:
                        break
                else:
                    maws[len(cand)].add(to_canonical(cand))


            cand = sub + a
            valid = False
            for seq in seqs:
                w = cand[1:] 
                if w in substrings or rev(w) in substrings:
                    valid = True
                    break
            if valid:
                for seq in seqs:
                    if cand in seq or rev(cand) in seq:
                        break
                else:
                    maws[len(cand)].add(to_canonical(cand))
          
    return maws