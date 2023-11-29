#! /usr/bin/env python3

import argparse
import collections
import os
import re
import sys

import xxhash # pip install --upgrade xxhash

# initialization:
# h=xxhash.xxh32(seed=0)
#
# hashing an element:
# h.reset()
# h.update(x)

def readfq(fp):  # this is a generator function
    # From https://github.com/lh3/readfq/blob/master/readfq.py
    last = None  # this is a buffer keeping the last unprocessed line
    while True:  # mimic closure; is it a bad idea?
        if not last:  # the first record or a record following a fastq
            for l in fp:  # search for the start of the next record
                if l[0] in '>@':  # fasta/q header line
                    last = l[:-1]  # save this line
                    break
        if not last: break
        name, seqs, last = last[1:].partition(" ")[0], [], None
        for l in fp:  # read the sequence
            if l[0] in '@+>':
                last = l[:-1]
                break
            seqs.append(l[:-1])
        if not last or last[0] != '+':  # this is a fasta record
            yield name, ''.join(seqs), None  # yield a fasta record
            if not last: break
        else:  # this is a fastq record
            seq, leng, seqs = ''.join(seqs), 0, []
            for l in fp:  # read the quality
                seqs.append(l[:-1])
                leng += len(l) - 1
                if leng >= len(seq):  # have read enough quality
                    last = None
                    yield name, seq, ''.join(seqs)
                    # yield a fastq record
                    break
            if last:  # reach EOF before reading enough quality
                yield name, seq, None  # yield a fasta record instead
                break


rc = str.maketrans({'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'})


def canonical(kmer):
    return min(kmer, kmer[::-1].translate(rc))


def read_kmers(fn, k):
    with open(fn) as fo:
        for name, seq, _ in readfq(fo):
            seq = seq.upper()
            for x in re.split(r'[^ACGT]', seq):
                for i in range(len(x) - k + 1):
                    yield canonical(x[i:i + k])


def main():
    pass


if __name__ == "__main__":
    main()
