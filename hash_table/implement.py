# Implement with array using linear probing

class HashTable:
    def __init__(self,capacity = 16):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
# hash(k, m) - m is the size of the hash table
    def hash_key(self,key,m):
        return hash(key) % m


# add(key, value) - if the key already exists, update value
    def add(self,key,value):
        index = self.hash_key(key,self.capacity)


        while self.table[index] is not None:
            stored_k,stored_v = self.table[index]

            if stored_k ==key:
                self.table[index] = (key,value)
                return
            
            index = (index+1) % self.capacity
        

        self.table[index] = (key, value)
        self.size += 1


# exists(key)
    def exists(self,key):
        index = self.hash_key(key,self.capacity)

        while self.table[index] is not None:
            stored_key, stored_value = self.table[index]

            if stored_key == key:
                return True
            
            index = (index+1) % self.capacity
        return False
    
# remove(key)
    def remove(self,key):
        index = self.hash_key(key,self.capacity)

        DELETED = object()

        for i in range(self.capacity):
            if self.table[index] is None:
                raise KeyError("key not found")
            
            if self.table[index] is not DELETED:
                stored_key, stored_value = self.table[index]

                if stored_key == key:
                    self.table[index] = DELETED
                    self.size-=1
                    return

            
            index = (index+1)% self.capacity
        
        raise KeyError("Key not found")