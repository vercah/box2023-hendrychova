import time
import sys
from maw.maw import read_fa_sequences
import maw.naive as naive
import maw.better as better
import maw.fast as fast
from maw.fmt import pprint, to_tsv
import matplotlib.pyplot as plt


seqs = read_fa_sequences(sys.argv[1])
seqs = set(seqs.values())
max_kmax = int(sys.argv[2])
kmax_vals = list(range(3, max_kmax+1))

time_data = {}
def benchmark(find_maws_fn, name):
    durations = []
    for kmax in kmax_vals:
        print(f"Benchmarking {name} for kmax = {kmax}")
        start_time = time.time()
        find_maws_fn(seqs, kmax)
        end_time = time.time()
        elapsed_time = end_time - start_time
        durations.append(elapsed_time)
    time_data[name] = durations

print("Starting benchmarking")
benchmark(naive.find_maws, "naive")
benchmark(better.find_maws, "better")
benchmark(fast.find_maws, "fast")
print("Done")


for name, durations in time_data.items():
    plt.plot(kmax_vals, durations, label=name, marker='o')
plt.xlabel('K max')
plt.ylabel('Elapsed Time (seconds)')
plt.title('Execution time for different kmax values')
plt.yscale("log")
plt.legend()
plt.savefig('benchmark.png')
plt.show()
