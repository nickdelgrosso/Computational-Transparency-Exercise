from collections import Counter
from pathlib import Path

import numpy as np

# Save Word Count, for each work, into a numpy file
data_dir = Path(".")
for f in data_dir.glob('data/**/*.txt'):
    try:
        text = f.read_text()
    except UnicodeDecodeError:
        continue
    words = "".join(c for c in text if c not in "\".;:,!$-'1234567890?[](){}><^%=_ã©&").replace('\n', ' ').lower().split()
    counts = Counter(words)
    np.save(f.with_suffix('.npy'), counts)