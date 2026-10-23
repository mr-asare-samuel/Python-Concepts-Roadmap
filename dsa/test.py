class Stack:
    def __init__(self):
        self._data = [] #private attribute

    
    def push(self, data):
        self._data.append(data)

    def pop(self):
        return self._data.pop()

    def get_data(self):
        return self._data

stack = Stack()
stack.push(34)
print(stack.get_data())


"""
Hash table:

separate chaining
random probing


Sets and Dictionaries both uses hash function to store data in memory
that make it not able to keep duplicates. two or more similar things gets 
the same hash code which makes its keep only the latest one.

"""


print([[] for _ in range(8)])

print(hash(8) % 8)


data = []

data.append(90)
data.append(40)
print(data)


import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 8)
heapq.heappush(heap, 3)
heapq.heappush(heap, 0)

print(heap)                 # 1, peek at the smallest
# print(heapq.heappop(heap))     # 1
# print(heapq.heappop(heap))     # 3
# print(heapq.heappop(heap))     # 5


nums = [9, 4, 7, 1, 8]
heapq.heapify(nums)            # in place, O(n)
print(nums)                 # 1
