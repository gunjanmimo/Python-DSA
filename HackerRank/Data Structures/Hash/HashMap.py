# %%
import uuid


class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def getHash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, val):
        key_hash = self.getHash(key)
        key_val = [key, val]
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_val])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = val
                    return True
            self.map[key_hash].append(key_val)
            return True

    def search(self, key):
        key_hash = self.getHash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair
        return None

    def delete(self, key):
        key_hash = self.getHash(key)
        if self.map[key_hash] is None:
            return False
        for index in range(0, len(self.map[key_hash])):
            if self.map[key_hash][index][0] == key:
                self.map[key_hash].pop(index)
                return True


# %%
if __name__ == "__main__":
    hashMap = HashMap()
    hashMap.add("Gunjan", str(uuid.uuid4()))
    hashMap.add("Paul", str(uuid.uuid4()))
    hashMap.add("Mimo", str(uuid.uuid4()))
    hashMap.add("Belgium", str(uuid.uuid4()))
    hashMap.add("Linkoping", str(uuid.uuid4()))
    hashMap.add("Sen", str(uuid.uuid4()))
    hashMap.add("Swiss", str(uuid.uuid4()))
    hashMap.add("Spain", str(uuid.uuid4()))
    hashMap.add("Korea", str(uuid.uuid4()))
    print(hashMap.search("Mimo"))
    print(hashMap.delete("Mimo"))
    print(hashMap.search("Mimo"))
# %%
