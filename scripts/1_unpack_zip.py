import zipfile

# Unpack Data
with zipfile.ZipFile("short_gutenberg.zip", 'r') as zip_ref:
    zip_ref.extractall(".")