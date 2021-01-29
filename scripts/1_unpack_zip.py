import zipfile

# Unpack Data
with zipfile.ZipFile("data/short_gutenberg.zip", 'r') as zip_ref:
    zip_ref.extractall("./data")