import hashlib
import time

class HashTable(object):

    def __init__(self, size=16):
        self.num_elements = 0
        self.data = [None] * size  # Use None instead of 0 to differentiate empty slots
        self.size = size
        self.resize_count = 0
        self.total_resize_time = 0

    def __get_hash_index(self, key):
        key_str = str(key)
        our_hash = int(hashlib.md5(key_str.encode()).hexdigest(), 16)
        return our_hash % self.size

    def __resize(self):
        start_time = time.time()
        new_size = self.size * 2
        new_data = [None] * new_size
        for bucket in self.data:
            if bucket is not None:
                for (k, v) in bucket:
                    new_hash_index = self.__get_hash_index(k)
                    if new_data[new_hash_index] is None:
                        new_data[new_hash_index] = [(k, v)]
                    else:
                        new_data[new_hash_index].append((k, v))
        self.data = new_data
        self.size = new_size
        self.resize_count += 1
        elapsed_time = time.time() - start_time
        self.total_resize_time += elapsed_time
        print(f"{self.size}, {elapsed_time:.10f}")

    def insert(self, key, value):
        hash_data = (key, value)
        hash_index = self.__get_hash_index(key)
        if self.data[hash_index] is None:
            self.data[hash_index] = [hash_data]
        else:
            self.data[hash_index].append(hash_data)
        self.num_elements += 1

    def __get_data_index_tuple(self, key):
        hash_index = self.__get_hash_index(key)
        bucket = self.data[hash_index]

        if bucket is not None:
            for data_index, (k, _) in enumerate(bucket):
                if k == key:
                    return (hash_index, data_index)
        return None

    def get(self, key):
        dit = self.__get_data_index_tuple(key)
        if dit:
            return self.data[dit[0]][dit[1]][1]
        raise KeyError("Hash key does not exist")

    def remove(self, key):
        dit = self.__get_data_index_tuple(key)
        if not dit:
            raise KeyError("Hash key does not exist")

        bucket = self.data[dit[0]]
        if len(bucket) == 1:
            self.data[dit[0]] = None
        else:
            del self.data[dit[0]][dit[1]]

        self.num_elements -= 1

    def key_contains(self, substring):
        raise NotImplementedError

start = time.time()

# Test the HashTable implementation
our_hash_table = HashTable()
names = []
for i in range(10_000_000):
    names.append(i)
name_tuples = [(n, f"{n}@gmail.com") for n in names]

for name_data in name_tuples:
    our_hash_table.insert(name_data[0], name_data)

print("Done")
