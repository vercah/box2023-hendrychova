import pytest
from maw.utils import reverse_complement
from maw.utils import to_canonical

def test_reverse_complement():
    assert reverse_complement("ACGT") == "ACGT"
    assert reverse_complement("AAAACCCC") == "GGGGTTTT"
    assert reverse_complement("AACTACT") == "AGTAGTT"

def test_to_canonical():
    assert to_canonical("ACGT") == "ACGT"
    assert to_canonical("AAAACCCC") == "AAAACCCC"
    assert reverse_complement("AGTAGTT") == "AACTACT"