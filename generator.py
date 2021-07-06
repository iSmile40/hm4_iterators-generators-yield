import hashlib

def hash_coutries(file_path):
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            string_hash = hashlib.md5(line.strip().encode()).hexdigest()
            yield string_hash

for string in hash_coutries('countries_wiki.txt'):
    print(string)
