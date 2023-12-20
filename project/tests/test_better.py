import pytest
from maw.better import k_substrings
from maw.better import all_substrings
from maw.better import add_reverse_complements


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
    

    