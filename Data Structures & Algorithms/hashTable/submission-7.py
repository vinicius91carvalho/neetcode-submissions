class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashTable:
    
    def __init__(self, capacity: int):
        self.map = []
        for i in range(capacity):
            self.map.append(None)
        self.size = 0
        self.capacity = capacity
    
    def hash(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        hash_key = self.hash(key)

        while True:
            if not self.map[hash_key] or self.map[hash_key].key == -1:
                self.map[hash_key] = Pair(key, value)
                self.size += 1
                break
            else:
                if self.map[hash_key].key == key:
                    self.map[hash_key].val = value
                    return
                
                hash_key += 1
                hash_key %= self.capacity
            
        if self.size / self.capacity >= 0.5: 
            self.resize()

    def get(self, key: int) -> int:
        hash_key = self.hash(key)


        while self.map[hash_key]:
            if self.map[hash_key].key == key:
                return self.map[hash_key].val
            hash_key += 1
        return -1

    def remove(self, key: int) -> bool:
        hash_key = self.hash(key)
        if not self.map[hash_key] or self.map[hash_key].key == -1:
            return False

        while self.map[hash_key]:
            if self.map[hash_key].key == key:
                self.map[hash_key] = Pair(-1,-1)
                self.size -= 1
                return True
            hash_key += 1
            hash_key %= self.capacity
        
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        tmp = self.map
        self.map = []
        self.capacity = 2 * self.capacity
        self.size = 0
        
        for i in range(self.capacity):
            self.map.append(None)
        
        for i in range(len(tmp)):
            if tmp[i]:
                self.insert(tmp[i].key, tmp[i].val)

