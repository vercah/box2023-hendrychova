import pytest
import maw.naive as naive
import maw.fast as fast

def test_fast_correct_1():
    seqs = {"ACGCCTAGTTTGGTGA"}
    assert fast.find_maws(seqs, 3) == naive.find_maws(seqs, 3)
    assert fast.find_maws(seqs, 4) == naive.find_maws(seqs, 4)
    assert fast.find_maws(seqs, 5) == naive.find_maws(seqs, 5)

def test_fast_correct_2():
    seqs = {"AAAAAAAAAA"}
    assert fast.find_maws(seqs, 3) == naive.find_maws(seqs, 3)
    assert fast.find_maws(seqs, 4) == naive.find_maws(seqs, 4)
    assert fast.find_maws(seqs, 5) == naive.find_maws(seqs, 5)

def test_fast_correct_3():
    # one "large" sequence
    seqs = {
        "GGTCTCTCTGGTTAGACCAGATCTGAGCCTGGGAGCTCTCTGGCTAACTAGGGAACCCACTGCTTAAGCC"
        "TCAATAAAGCTTGCCTTGAGTGCTTCAAGTAGTGTGTGCCCGTCTGTTGTGTGACTCTGGTAACTAGAGA"
        "TCCCTCAGACCCTTTTAGTCAGTGTGGAAAATCTCTAGCAGTGGCGCCCGAACAGGGACCTGAAAGCGAA"
        "AGGGAAACCAGAGGAGCTCTCTCGACGCAGGACTCGGCTTGCTGAAGCGCGCACGGCAAGAGGCGAGGGG"
        "CGGCGACTGGTGAGTACGCCAAAAATTTTGACTAGCGGAGGCTAGAAGGAGAGAGATGGGTGCGAGAGCG"
        "TCAGTATTAAGCGGGGGAGAATTAGATCGATGGGAAAAAATTCGGTTAAGGCCAGGGGGAAAGAAAAAAT"
        "ATAAATTAAAACATATAGTATGGGCAAGCAGGGAGCTAGAACGATTCGCAGTTAATCCTGGCCTGTTAGA"
    }
    assert fast.find_maws(seqs, 3) == naive.find_maws(seqs, 3)
    assert fast.find_maws(seqs, 4) == naive.find_maws(seqs, 4)
    assert fast.find_maws(seqs, 5) == naive.find_maws(seqs, 5)


def test_fast_correct_4():
    seqs = {
        "GGTCTCTCTGGTTAGACCAGATCTGAGCCTGGGAGCTCTCTGGCTAACTAGGGAACCCACTGCTTAAGCC",
        "TCAATAAAGCTTGCCTTGAGTGCTTCAAGTAGTGTGTGCCCGTCTGTTGTGTGACTCTGGTAACTAGAGA",
        "TCCCTCAGACCCTTTTAGTCAGTGTGGAAAATCTCTAGCAGTGGCGCCCGAACAGGGACCTGAAAGCGAA",
        "AGGGAAACCAGAGGAGCTCTCTCGACGCAGGACTCGGCTTGCTGAAGCGCGCACGGCAAGAGGCGAGGGG",
        "CGGCGACTGGTGAGTACGCCAAAAATTTTGACTAGCGGAGGCTAGAAGGAGAGAGATGGGTGCGAGAGCG",
        "TCAGTATTAAGCGGGGGAGAATTAGATCGATGGGAAAAAATTCGGTTAAGGCCAGGGGGAAAGAAAAAAT",
        "ATAAATTAAAACATATAGTATGGGCAAGCAGGGAGCTAGAACGATTCGCAGTTAATCCTGGCCTGTTAGA"
    }
    assert fast.find_maws(seqs, 3) == naive.find_maws(seqs, 3)
    assert fast.find_maws(seqs, 4) == naive.find_maws(seqs, 4)
    assert fast.find_maws(seqs, 5) == naive.find_maws(seqs, 5)