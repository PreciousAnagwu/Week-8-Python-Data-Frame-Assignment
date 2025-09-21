import chardet

with open("metadata.csv", "rb") as f:
    raw_data = f.read(100000)  # read first 100 KB
    result = chardet.detect(raw_data)
    print(result)
