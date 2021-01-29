import pickle
from collections import Counter
from pathlib import Path

import numpy as np

# Sum Word Counts
data_dir = Path("./data/3_word_counts")
total_counts = Counter()
for f in data_dir.glob('*.npy'):
    data = np.load(f, allow_pickle=True)
    dd = dict(data.item())
    total_counts += Counter(dd)

final_dir = Path("./data/4_final_word_count")
final_dir.mkdir(exist_ok=True, parents=True)
final_file = final_dir / "total_word_counts"
with final_file.with_suffix('.pkl').open('wb') as pickle_file:
    pickle.dump(total_counts, pickle_file)