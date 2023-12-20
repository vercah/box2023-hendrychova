from maw.utils import reverse_complement, to_canonical
from maw.utils import ALPHABET

def is_maw(x: str, sequences: set[str]):
    """Tests if a given word x is a minimmal absent word of the given
    sequences. Mostly for testing purposes.
    """

    # |x| >= 3
    if len(x) < 3:
        return False
    
    # x is an absent word
    rx = reverse_complement(x)
    for seq in sequences:
        if x in seq or rx in seq:
            return False
    
    # for all proper substrings w of x (|w| < |x|), w or its
    # reverse complement is a substring of at least one of
    # the sequences
    for wl in range(1, len(x)): # |w| = 1..|x|-1
        for wi in range(0, len(x)-wl): # start index of w
            w = x[wi:wi+wl]
            rw = reverse_complement(w)
            in_sequence = False
            for seq in sequences:
                if w in seq or rw in seq:
                    in_sequence = True
                    break
            if not in_sequence:
                return False
    
    return True

def increment_lexicographic(array: list[int], base: int):
    i = len(array) - 1
    while i >= 0:
        array[i] += 1
        if array[i] == base:
            array[i] = 0
            i -= 1
        else:
            break
    return i >= 0

def generate_lexicographic(alphabet: str, size: int):
    letters = sorted(alphabet)
    array = [0] * size
    def array_string():
        return "".join(letters[a] for a in array)
    yield array_string()
    while increment_lexicographic(array, len(letters)):
        yield array_string()


def find_maws(sequences: set[str], kmax: int) -> dict[int, set[str]]:
    """Returns all minimum absent words (MAWs) of length 3 to kmax of the set
    of sequences. Each set of MAWs contains only the canonical strings.
    
    Returns: a dictionary `maws` such that `maws[k]` is the set of MAWs
    of length k in the set of sequences.
    """
    maws = {k: set() for k in range(3, kmax+1)}
    for k in maws.keys():
        for x in generate_lexicographic(ALPHABET, k):
            if is_maw(x, sequences):
                maws[k].add(to_canonical(x))
    return maws