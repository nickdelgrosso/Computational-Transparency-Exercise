from collections import Counter
from pathlib import Path

import numpy as np

# Save Word Count, for each work, into a numpy file
data_dir = Path("data/2_extracted")
output_dir = Path("data/3_word_counts")
for f in data_dir.glob('**/*.txt'):
    try:
        text = f.read_text()
    except UnicodeDecodeError:
        continue
    words = "".join(c for c in text if c not in "\".;:,!$-'1234567890?[](){}><^%=_ã©&").replace('\n',
                                                                                                ' ').lower().split()
    counts = Counter(words)
    np.save(output_dir.joinpath(f.name).with_suffix('.npy'), counts)
