from __future__ import annotations
from maw.karkkainen_sanders import simple_kark_sort
from maw.utils import ALPHABET
from maw.utils import reverse_complement
from maw.utils import to_canonical


def build_lcp(s: str, sa: list[int]):
    n = len(s)
    rank = [0] * n
    for i in range(n):
        rank[sa[i]] = i
    k = 0
    lcp = [0] * (n-1)
    for i in range(n):
        if rank[i] == n - 1:
            k = 0
            continue
        j = sa[rank[i] + 1]
        while i + k < n and j + k < n and s[i+k] == s[j+k]:
            k += 1
        lcp[rank[i]] = k
        if k != 0:
            k -= 1
    return lcp

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
        self.lcp = build_lcp(seq, self.sa)
    
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
    
    def substrings(self, mini: int, maxi: int):
        sa = self.sa
        n = len(sa)
        suf_len = [n - sa[i] for i in range(n)]
        i = 0
        while i < n:
            if suf_len[i] < mini:
                i += 1
                continue
            start_len = mini
            if i > 0:
                start_len = max(start_len, self.lcp[i-1])
            for l in range(start_len, min(suf_len[i], maxi)+1):
                yield sa[i], l
            i += 1

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

    subs = {k: set() for k in range(2, kmax+1)}
    for s, seq in enumerate(seqs):
        # print(f"Gathering substrings of sequence {s}")
        for i, l in seq.substrings(2, kmax):
            subs[l].add(seq[i:i+l])
    
    for k in range(2, kmax):
        for sub in subs[k]:
            for a in ALPHABET:
                cand = a + sub
                w = cand[:-1]
                if (w in subs[k] or rev(w) in subs[k]) and \
                    cand not in subs[k+1] and rev(cand) not in subs[k+1]:
                    maws[k+1].add(to_canonical(cand))

                cand = sub + a
                w = cand[1:]
                if (w in subs[k] or rev(w) in subs[k]) and \
                    cand not in subs[k+1] and rev(cand) not in subs[k+1]:
                    maws[k+1].add(to_canonical(cand))
    return maws