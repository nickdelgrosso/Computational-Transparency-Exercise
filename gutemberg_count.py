
import json
from pathlib import Path
import shutil
import zipfile
from collections import Counter
import matplotlib.pyplot as plt
from tqdm import tqdm
import pickle
import pandas as pd


# Unpack Data
with zipfile.ZipFile("short_gutenberg.zip", 'r') as zip_ref:
    zip_ref.extractall(".")
    
# Save Word Count, for each work, into a json file
data_dir = Path(".")
for f in data_dir.glob('**/*.txt'):
    try:
        text = f.read_text()
    except UnicodeDecodeError:
        continue
    words = "".join(c for c in text if c not in "\".;:,!$-'1234567890?[](){}><^%=_ã©&").replace('\n', ' ').lower().split()
    counts = Counter(words)
    with f.with_suffix('.json').open('w') as json_file:
        json.dump(counts, json_file)
    
# Sum Word Counts
data_dir = Path(".")
total_counts = Counter()
for f in data_dir.glob('**/*.json'):
    total_counts += Counter(json.load(f.open('r')))

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

