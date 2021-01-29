import zipfile

# Unpack Data
with zipfile.ZipFile("data/1_raw/short_gutenberg.zip", 'r') as zip_ref:
    zip_ref.extractall("./data/2_extracted")