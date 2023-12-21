import time
import sys
from maw.maw import read_fa_sequences
from maw.naive import find_maws as maws_naive
from maw.better import find_maws as maws_better
from maw.fmt import pprint, to_tsv
import matplotlib.pyplot as plt

sequences = read_fa_sequences(sys.argv[1])
max_kmax = int(sys.argv[2])
time_data = {}

for kmax in range(1, max_kmax+1):
    start_time = time.time()
    maws = maws_naive(set(sequences.values()), kmax)
    end_time = time.time()
    elapsed_time = end_time - start_time
    time_data[kmax] = elapsed_time

# Separate the parameter values and measured times for plotting
sorted_keys = sorted(time_data.keys())
sorted_values = [time_data[key] for key in sorted_keys]

# Plotting the data
plt.plot(sorted_keys, sorted_values, marker='o')
plt.xlabel('K max')
plt.ylabel('Elapsed Time (seconds)')
plt.title('Execution time of naive solution')
plt.savefig('naive.png')
plt.show()
