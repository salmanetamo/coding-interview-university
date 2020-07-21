class HashTable:
    def __init__(self, m=16):
        self.m = m
        self.values = [None] * m
        self.keys = [None] * m

    def hash(self, key, m):
        key_as_int = sum([ord(char) for char in key])
        return key_as_int % m

    def add(self, key, value):
        hash = self.hash(key, self.m)
        if not self.keys[hash]:
            self.keys[hash] = key
            self.values[hash] = value
        else:
            if self.keys[hash] == key:
                self.values[hash] = value
            else:
                new_hash = self.hash(hash, self.m + 1)
                while not self.keys[new_hash] and self.keys[new_hash] != key:
                    new_hash = self.hash(new_hash, self.m + 1)

                self.keys[new_hash] = key
                self.values[new_hash] = value

    # def exists(self, key):
    #     return self.hash(key) < self.m
    #
    # def get(self, key):
    #     if not self.exists(key):
    #         raise KeyError('Key not found')
    #     hash = self.hash(key, self.m)
    #     return self.values[hash]
    #
    # def remove(self, key):
    #     if not self.exists(key):
    #         raise KeyError('Key not found')
    #     hash = self.hash(key, self.m)
    #     self.values[hash] = None
