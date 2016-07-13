class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size #sets every cells to None

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]: #check if the key and value is already existing
                if pair[0] == key:
                    pair[1] == value
                    return True
                self.map[key_hash].append(key_value) #did not find a match for the key
                return True

    def get(self, key):
        key_hash = self._get_hash(key):
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):


    def print(self)
