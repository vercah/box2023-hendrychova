import time
import sys
from maw.readfa import read_fa_sequences
import maw.naive as naive
import maw.better as better
import maw.fast as fast
from maw.fmt import pprint, to_tsv
import matplotlib.pyplot as plt


filename = sys.argv[1]
print(f"Loading {filename}")
seqs = read_fa_sequences(filename)
max_kmax = int(sys.argv[2])
kmax_vals = list(range(3, max_kmax+1))

try:
    max_seqs = int(sys.argv[3])
    seqs = set(list(seqs)[:max_seqs])
except:
    pass


print(f"{len(seqs)} sequences")

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
plt.title(f'Execution times for {filename}, {len(seqs)} sequences')
plt.yscale("log")
plt.legend()
plt.savefig(f'benchmark-{filename.split(".")[0]}-k{max_kmax}.png')
plt.show()
