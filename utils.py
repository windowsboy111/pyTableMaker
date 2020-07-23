# https://stackoverflow.com/questions/4326658/how-to-index-into-a-dictionary
# this can allows getting dictionary keys / values by numerical keys
def get_key(dictionary: dict, n: int = 0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range")


def dict_indexing(dictionary: dict):
    return list(dictionary.items())


def main():
    print(dict_indexing({"a": 1, "b": "hello"}))


if __name__ == '__main__':
    main()
