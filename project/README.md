# Minimal Absent Words

This project implements several algorithms to experiment with he extraction
of minimal absent words (MAW) from a set of sequences provided in a FASTA file.

## Install

Clone this repository, and in this project folder enter:

```bash
pip install -r requirements.txt
python setup.py build
pip install -e .
```

## Usage

Basic usage:

```bash
maw -f sequences.fa --kmax 6 -t maws.tsv
```

Documentation:

```bash
maw -h
```
```
usage: maw [-h] -f FILE -k KMAX [-a {naive,string-ext,fast-string-ext}] [-p] [-t TSV] [-s SAMPLE]

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Source FASTA file, can be compressed.
  -k KMAX, --kmax KMAX
  -a {naive,string-ext,fast-string-ext}, --algo {naive,string-ext,fast-string-ext}
                        What algorithm to use
  -p, --print           Set if you want to display the result in the console as well.
  -t TSV, --tsv TSV     Name of the output TSV file.
  -s SAMPLE, --sample SAMPLE
                        Compute on a subset of the given size of the whole sequences set.
```

## Testing

### Unit tests

Unittests require `pytest` (installed with the requirements). Run all
the tests with:

```bash
python -m pytest tests
```

### Benchmarks

The `benchmark.py` script allows you to compare the different algorithms on a given dataset.

Use it as follows:

```bash
python benchmark.py FILE MAX_KMAX [SAMPLES]
```

where

- `FILE` is the path to the FASTA file to run the benchmark on;
- `MAX_KMAX` reprsents the last `kmax` value for which the algorithms will be run. The
script measures the execution time for all `kmax` between `3` and `MAX_KMAX`;
- `SAMPLES` (optional) specify the number of sequences to consider from the FASTA file
for the benchmark. If not set, all the sequences are considered.

At the end of the benchmark, a plot will be displayed and saved into a PNG.
