from __future__ import annotations
from maw.karkkainen_sanders import simple_kark_sort
from maw.utils import ALPHABET
from maw.utils import reverse_complement
from maw.utils import to_canonical
from functools import cached_property

# class View:
#     def __init__(self, seq: str, i: int, j: int) -> None:
#         if i < 0 or i >= len(seq) or j < 0 or j > len(seq):
#             raise IndexError("Index out of range.")
#         if i > j:
#             raise ValueError("Invalid view range.")
#         self.seq = seq
#         self.i = i
#         self.j = j
    
#     def __str__(self):
#         return self.seq[self.i:self.j]

#     def __getitem__(self, i: int) -> str:
#         k = self.i + i
#         if k < self.i or k >= self.j:
#             raise IndexError("Index out of range.")
#         return self.seq[self.i + i]
    
#     def __len__(self) -> int:
#         return self.j - self.i
    
#     def view(self, i: int, j: int) -> View:
#         i1 = self.i + i
#         j1 = self.i + j
#         if i1 < self.i or i1 >= self.j or \
#             j1 < self.j or j1 >= self.j:
#             raise IndexError("Index out of range.")
#         return View(self.seq, i1, j1)
    
#     def startswith(self, sub: str) -> bool:
#         if len(sub) > len(self):
#             return False
#         for k in range(len(sub)):
#             if self.seq[self.i + k] != sub[k]:
#                 return False
#         return True
    
#     def compare_with(self, other: str) -> int:
#         for k in range(min(len(other), len(self))):
#             if self.seq[self.i + k] < other[k]:
#                 return -1
#             elif self.seq[self.i + k] > other[k]:
#                 return 1
#         if len(self) < len(other):
#             return -1
#         elif len(self) > len(other):
#             return 1
#         else:
#             return 0


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


def k_maws_of_seq(s: Sequence, k: int) -> set[str]:
    k_maws = set()
    tested = set()
    rev = reverse_complement

    for i in range(0, len(s)-(k-2)+1):
        w0 = s[i:i+(k-2)]
        if w0 in tested:
            continue
        tested.add(w0)
        
        for a in ALPHABET:
            wl = a + w0
            if wl not in s and rev(wl) not in s:
                continue

            for b in ALPHABET:
                wr = w0 + b
                if wr not in s and rev(wr) not in s:
                    continue
                
                fx = a + w0 + b
                rx = rev(fx)
                if fx in s or rx in s:
                    continue
                k_maws.add(fx)
                k_maws.add(rx)
    
    return k_maws


def find_maws(sequences: set[str], kmax: int) -> dict[int, set[str]]:
    """Returns all minimum absent words (MAWs) of length 3 to kmax of the set
    of sequences. Each set of MAWs contains only the canonical strings.
    
    Returns: a dictionary `maws` such that `maws[k]` is the set of MAWs
    of length k in the set of sequences.
    """
    maws = {k: set() for k in range(3, kmax+1)}

    seqs = []
    for i, s in enumerate(sequences):
        # print(f"Initializing sequence {i}")
        seqs.append(Sequence(s))
    # seqs = set(map(Sequence, sequences))
    for k in maws.keys():
        for i, seq in enumerate(seqs):
            # print(f"Finding {k}-MAWs of sequence {i}")
            for maw in k_maws_of_seq(seq, k):
                add = True
                for other in seqs:
                    if maw in other:
                        add = False
                        break
                if add:
                    maws[k].add(to_canonical(maw))
                
    return maws