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
        hash_data = (key, value)
        hash_index = self.__get_hash_index(key)
        self.data[hash_index] = hash_data
        self.num_elements += 1

    def get(self, key):
        hash_index = self.__get_hash_index(key)
        data = self.data[hash_index]
        dk = data[0]
        if key != dk or data == 0:
            raise KeyError("Hash key does not exist")
        return data[1]
        
        

    def remove(self, key):
        hash_index = self.__get_hash_index(key)
        data = self.data[hash_index]
        dk = data[0]
        if key != dk or data == 0:
            raise KeyError("Hash key does not exist")
        self.data[hash_index] = 0
        self.num_elements -= 1

    def key_contains(self, substring): #Extra thing he is doing that 
        pass        


hash = HashTable()
hash.insert( 0, 3.14159)
print("== Insert data ==")
print(hash.data)
print(hash.num_elements)
print(hash.get(0))