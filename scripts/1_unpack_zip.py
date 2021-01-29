import zipfile

# Unpack Data
with zipfile.ZipFile("data/raw/short_gutenberg.zip", 'r') as zip_ref:
    zip_ref.extractall("./data")