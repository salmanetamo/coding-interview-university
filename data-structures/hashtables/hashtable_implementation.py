class HashTable:
    def __init__(self, m=16):
        self.m = m
        self.values = [None] * m
        self.keys = [None] * m

    def hash(self, key, size):
        key_as_int = sum([ord(char) for char in key])
        return key_as_int % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def add(self, key, value):
        hash = self.hash(key, self.m)
        if not self.keys[hash]:
            self.keys[hash] = key
            self.values[hash] = value
        else:
            if self.keys[hash] == key:
                self.values[hash] = value
            else:
                new_hash = self.rehash(hash, self.m)
                while self.keys[new_hash] and self.keys[new_hash] != key:
                    new_hash = self.rehash(new_hash, self.m)

                self.keys[new_hash] = key
                self.values[new_hash] = value

    def exists(self, key):
        hash = self.hash(key, self.m)
        return hash < len(self.keys) and self.keys[hash] is not None

    def get(self, key):
        start_hash = self.hash(key, self.m)
        value = None
        found = False
        stop = False
        current_hash = start_hash

        while self.keys[current_hash] is not None and not found and not stop:
            if self.keys[current_hash] == key:
                found = True
                value = self.values[current_hash]
            else:
                current_hash = self.rehash(current_hash, self.m)
                if current_hash == start_hash:
                    stop = True
        return value

    def remove(self, key):
        if not self.exists(key):
            raise KeyError('Key not found')

        start_hash = self.hash(key, self.m)
        found = False
        stop = False
        current_hash = start_hash

        while self.keys[current_hash] is not None and not found and not stop:
            if self.keys[current_hash] == key:
                self.keys[current_hash] = None
                self.values[current_hash] = None
                found = True
            else:
                current_hash = self.rehash(current_hash, self.m)
                if current_hash == start_hash:
                    stop = True
