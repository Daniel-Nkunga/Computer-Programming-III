import hashlib

class HashTable(object):
    def __init__(self, size = 3): #Size should porblaby need to be removed
        self.num_elements = 0 #Number of elements in the table
        self.data = [0] * size
        self.size = len(self.data) #Allows for incrimental resizing
        print(self.data)

    def __get_hash_index(self, key):
        key_str = str(key)
        our_hash =  int(hashlib.md5(key_str.encode()).hexdigest(), 16)
        return our_hash % self.size
        
    def __resize(self):
        raise NotImplementedError

    def insert(self, key, value):
        hash_data = (key, value)
        hash_index = self.__get_hash_index(key)
        
        if self.data[hash_index] == 0:
            self.data[hash_index] = [hash_data]
        else:
            self.data[hash_index].append(hash_data)
        self.num_elements += 1

    def __get_data_index_tuple(self, key):
        hash_index = self.__get_hash_index(key)
        data_list = self.data[hash_index]
        if data_list == 0:
            return None
        for data_index, data in enumerate(data_list):
            dk = data[0]
            if dk == key:
                return (hash_index, data_index)
        

    def get(self, key):
        dit = self.__get_data_index_tuple(key)
        if dit:
            return self.data[dit[0]][dit[1]][1]
        raise KeyError("Hash key does not exist")

    def remove(self, key):
        dit = self.__get_data_index_tuple(key)
        if not dit:
            raise KeyError("Hash key does not exist")
        if len(self.data[dit[0]]) == 1:
            self.data[dit[0]] = 0
        else:
            del self.data[dit[0]][dit[1]]
        self.num_elements -= 1

    def key_contains(self, substring): #Extra thing he is doing that 
        raise NotImplementedError        


our_hash_table = HashTable()
names = ["Jim", "Mark","Steve", "Tony", "Jimbo", "Jimbob", "Havana", "Rashesh"]
name_tuples = [(n,f"{n}@gmail.com") for n in names]
 
for name_data in name_tuples:
    our_hash_table.insert(name_data[0], name_data)
print("== Insert data ==")
print(our_hash_table.data)
print(our_hash_table.num_elements)
print("==Get data==")
print(our_hash_table.get("Jim"))
print("== Remove data==")
our_hash_table.remove("Jim")
print(our_hash_table.data)
our_hash_table.remove("Mark")
print(our_hash_table.data)
print(our_hash_table.num_elements)