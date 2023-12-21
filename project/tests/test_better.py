import pytest
from maw.better import k_substrings
from maw.better import all_substrings
from maw.better import add_reverse_complements
from maw.better import get_proper_prefixes
from maw.better import get_proper_suffixes
from maw.better import extended_right
from maw.better import extended_left
from maw.better import get_all_maws
from maw.better import left_maw_candidates

def test_k_substrings():
    assert k_substrings("AACTGG", 2) == {"AA", "AC", "CT", "TG", "GG"}
    assert k_substrings("AACTGG", 3) == {"AAC", "ACT", "CTG", "TGG"}

def test_all_substrings():
    assert all_substrings("AACTGG", 2, 3) == {"AA", "AC", "CT", "TG", "GG", "AAC", "ACT", "CTG", "TGG"}
    assert all_substrings("ACCTG", 3, 5) == {"ACC", "CCT", "CTG", "ACCT", "CCTG", "ACCTG"}

def test_add_reverse_complements():
    assert add_reverse_complements({"AA", "AC", "CT", "TG", "GG", "AAC", "ACT", "CTG", "TGG"}) == {"AA", "AC", "CT", "TG", "GG", "AAC", "ACT", "CTG", "TGG", "TT", "GT", "AG", "CA", "CC", "GTT", "AGT", "CAG", "CCA"}
    
def test_get_proper_prefixes():
    assert get_proper_prefixes("CGAACT") == {"C", "CG", "CGA", "CGAA", "CGAAC"}
    assert get_proper_prefixes("CGACT") == {"CGAC", "CGA", "CG", "C"}

def test_get_proper_suffixes():
    assert get_proper_suffixes("AGGCTA") == {"A", "TA", "CTA", "GCTA", "GGCTA"}
    assert get_proper_suffixes("GTCCAT") == {"T", "AT", "CAT", "CCAT", "TCCAT"}

def test_extended_left():
    assert extended_left("TGAC") == {"ATGAC", "CTGAC", "GTGAC", "TTGAC"}

def test_extended_right():
    assert extended_right("TGAC") == {"TGACA", "TGACC", "TGACG", "TGACT"}

def test_left_maw_candidates():
    assert left_maw_candidates("AAC",3) == {"AAA", "CAA", "GAA", "TAA", "AAC", "CAC", "GAC", "TAC", "ATT", "CTT", "GTT", "TTT", "AGT", "CGT", "GGT", "TGT"}

def test_get_all_maws():
    assert get_all_maws({"AACTACT"}, 3) == {"AAA", "TAA", "AAG"}
    assert get_all_maws({"AAA"}, 3) == set()
