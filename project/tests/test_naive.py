import pytest
from maw.naive import is_maw

def test_is_maw():
    assert is_maw("GGA", {"ACCG"}) == False
    assert is_maw("CAC", {"ACCG"}) == False
    assert is_maw("CCC", {"ACCG"}) == True
    assert is_maw("ACG", {"ACCG"}) == True
    assert is_maw("AAA", {"AACTACT"}) == True
    assert is_maw("TAA", {"AACTACT"}) == True
