import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

total_counts = np.load("total_word_counts.pkl", allow_pickle=True)

# Plot Most Common Words
plt.figure()
plt.barh(*zip(*total_counts.most_common(20)))
plt.title("Most Common Words in Dataset")
plt.savefig("counts.png")

# # Compare Conjunctions
tc = pd.Series(total_counts)
plt.figure()
tc[['and', 'but', 'or']].plot.bar(rot=0)
plt.savefig("conjunctions_freq.png")

# # Yes vs No
tc[['yes', 'no']].plot.bar(rot=0)
plt.figure()
plt.savefig("affirmative_freq.png")

