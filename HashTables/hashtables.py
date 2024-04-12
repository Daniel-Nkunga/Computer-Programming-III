import hashlib

class HashTable(object):
    def __init__(self, size = 10): #Size should porblaby need to be removed
        self.num_elements = 0 #Number of elements in the table
        self.data = [0] * size
        self.size = len(self.data) #Allows for incrimental resizing
        print(self.data)

    def __get_hash_index(self, key):
        key_str = str(key)
        our_hash =  int(hashlib.md5(key_str.encode()).hexdigest(), 16)
        return our_hash % self.size
        
    def __resize(self):
        pass

    def insert(self, key, value):
        pass

    def get(self, key):
        pass

    def remove(self, key):
        pass

    def key_contains(self, substring): #Extra thing he is doing that 
        pass        


hash = HashTable()