class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for n in range(self.MAX)]

    def get__hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    # Methods    

    # def add(self, key, value):
    #     h = self.get__hash(key)
    #     self.arr[h] = value

    # def get(self, key):
    #     h = get__hash(key)
    #     return self.arr[h]


    # Getters and Setters

    def __setitem__(self, key, value):
        h = self.get__hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get__hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get__hash(key)
        self.arr[h] = None



# hm = HashTable()
# print(hm.arr)

# # hm.add('march 20', 500)

# hm['june 4'] = 40

# print(hm.arr)

# print(hm['june 4'])

# del hm['june 4']

# print(hm.arr)



"""
Collusion in hashtable is handle in two ways:
- Linear Probing
- Linked List at a location
"""

# Handling Collision with a list (chaining) at each bucket

class HashTable2:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for n in range(self.MAX)]   # each bucket is a plain list of (key, value) tuples

    def get__hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX


    def __setitem__(self, key, value):
        h = self.get__hash(key)                            # bucket index for this key
        found = False
        for idx, element in enumerate(self.arr[h]):         # scan the bucket's (key, value) pairs
            if element[0] == key:                           # same key already in this bucket?
                self.arr[h][idx] = (key, value)              # update in place
                found = True
                break

        if not found:
            self.arr[h].append((key, value))                # new key -> append to the bucket


    def __getitem__(self, key):
        h = self.get__hash(key)                             # bucket index for this key
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]                                 # not in the bucket at all

    def __delitem__(self, key):
        h = self.get__hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
                              

t = HashTable2()
t['march 6'] = 120
t['march 6'] = 78
t['march 14'] = 67
t['march 9'] = 4
t['march 17'] = 456

# 'march 6' and '6 march' are anagrams -> same characters -> same sum of
# ord() values -> same hash index -> they collide, landing in the same bucket
t['6 march'] = 999

print(t.get__hash('march 6'))
print(t.get__hash('6 march'))
print(t.arr[t.get__hash('march 6')])   # the colliding bucket: both entries

print(t.arr)

print(t['6 march'])
del t['6 march']

print(t.arr)
