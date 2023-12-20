import pytest
from maw.better import k_substrings
from maw.better import all_substrings
from maw.better import add_reverse_complements
from maw.better import get_proper_prefixes
from maw.better import get_proper_suffixes
from maw.better import extended_strings

def test_k_substrings():
    assert k_substrings("AACTGG", 2) == {"AA", "AC", "CT", "TG", "GG"}
    assert k_substrings("AACTGG", 3) == {"AAC", "ACT", "CTG", "TGG"}

def test_all_substrings():
    assert all_substrings("AACTGG", 2, 3) == {"AA", "AC", "CT", "TG", "GG",
                                             "AAC", "ACT", "CTG", "TGG"}
    assert all_substrings("ACCTG", 3, 5) == {"ACC", "CCT", "CTG", "ACCT", "CCTG",
                                             "ACCTG"}

def test_add_reverse_complements():
    assert add_reverse_complements({"AA", "AC", "CT", "TG", "GG", "AAC", 
                                    "ACT", "CTG", "TGG"}) == {"AA", "AC", "CT", "TG", "GG", "AAC", 
                                    "ACT", "CTG", "TGG", "TT", "GT", "AG", "CA", "CC", "GTT", 
                                    "AGT", "CAG", "CCA"}
    
def test_get_proper_prefixes():
    assert get_proper_prefixes("CGAACT") == {"C", "CG", "CGA", "CGAA", "CGAAC"}
    assert get_proper_prefixes("CGACT") == {"CGAC", "CGA", "CG", "C"}

def test_get_proper_suffixes():
    assert get_proper_suffixes("AGGCTA") == {"A", "TA", "CTA", "GCTA", "GGCTA"}
    assert get_proper_suffixes("GTCCAT") == {"T", "AT", "CAT", "CCAT", "TCCAT"}

def test_extended_strings():
    assert extended_strings("TGAC") == {"ATGAC", "CTGAC", "GTGAC", "TTGAC", "TGACA",
                                        "TGACC", "TGACG", "TGACT"}