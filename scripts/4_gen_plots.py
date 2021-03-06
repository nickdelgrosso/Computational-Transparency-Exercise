import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path

total_counts = np.load("./data/4_final_word_count/total_word_counts.pkl", allow_pickle=True)

# Plot Most Common Words
plt.figure()
plt.barh(*zip(*total_counts.most_common(20)))
plt.title("Most Common Words in Dataset")

Path("results").mkdir(exist_ok=True, parents=True)
plt.savefig("results/counts.png")

# # Compare Conjunctions
tc = pd.Series(total_counts)
plt.figure()
tc[['and', 'but', 'or']].plot.bar(rot=0)
plt.savefig("results/conjunctions_freq.png")

# # Yes vs No
tc[['yes', 'no']].plot.bar(rot=0)
plt.figure()
plt.savefig("results/affirmative_freq.png")

