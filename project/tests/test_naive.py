import pytest
from maw.naive import is_maw
from maw.naive import find_maws

def test_is_maw():
    assert is_maw("GGA", {"ACCG"}) == False
    assert is_maw("CAC", {"ACCG"}) == False
    assert is_maw("CCC", {"ACCG"}) == True
    assert is_maw("ACG", {"ACCG"}) == True
    assert is_maw("AAA", {"AACTACT"}) == True
    assert is_maw("TAA", {"AACTACT"}) == True

def find_maws():
    assert find_maws({"AACTACT"}, 3) == {3: {"AAA", "TAA", "AAG"}}
    assert find_maws({"AAA"}, 3) == dict()