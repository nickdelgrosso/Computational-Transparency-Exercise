
from pathlib import Path
import zipfile
from collections import Counter
import matplotlib.pyplot as plt
import pickle
import pandas as pd
import numpy as np

# Unpack Data
with zipfile.ZipFile("short_gutenberg.zip", 'r') as zip_ref:
    zip_ref.extractall(".")
    
# Save Word Count, for each work, into a numpy file
data_dir = Path(".")
for f in data_dir.glob('**/*.txt'):
    try:
        text = f.read_text()
    except UnicodeDecodeError:
        continue
    words = "".join(c for c in text if c not in "\".;:,!$-'1234567890?[](){}><^%=_ã©&").replace('\n', ' ').lower().split()
    counts = Counter(words)
    np.save(f.with_suffix('.npy'), counts)
    
# Sum Word Counts
data_dir = Path(".")
total_counts = Counter()
for f in data_dir.glob('**/*.npy'):
    data = np.load(f.with_suffix('.npy'), allow_pickle=True)
    dd = dict(data.item())
    total_counts += Counter(dd)

final_dir = Path(".")
final_dir.mkdir(exist_ok=True, parents=True)
final_file = final_dir / "total_word_counts"
with final_file.with_suffix('.pkl').open('wb') as pickle_file:
    pickle.dump(total_counts, pickle_file)

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

