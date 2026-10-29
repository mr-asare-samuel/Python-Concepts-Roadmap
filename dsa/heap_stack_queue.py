# Stack
"""
stack = []

stack.append(1)     # push
stack.append(2)
stack.append(3)

print(stack[-1])    # peek: 3
print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack)        # [1]

"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


# ------------------

from collections import deque

stk = deque()
stk.append("first")
stk.append(56)
stk.append(7)
stk.append("last")

print("Stack",stk)

stk.pop()
print(stk)


# QUEUE

"""
from collections import deque

queue = deque()

queue.append("Ama")      # enqueue
queue.append("Kofi")
queue.append("Yaw")

print(queue[0])          # peek: Ama
print(queue.popleft())   # dequeue: Ama
print(queue.popleft())   # Kofi
print(queue)             # deque(['Yaw'])

"""

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


# ---------------
from collections import deque

q = deque()

q.appendleft("start")
q.appendleft(15)
q.appendleft(12)
q.appendleft("end")

print("Queue", q)

q.pop()

print(q)

#Heap..........

"""

Python's heapq module is a min-heap built on a plain list.

"""


import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 8)
heapq.heappush(heap, 3)

print(heap[0])                 # 1, peek at the smallest
print(heapq.heappop(heap))     # 1
print(heapq.heappop(heap))     # 3
print(heapq.heappop(heap))     # 5


"""
Turn an existing list into a heap:
"""

nums = [9, 4, 7, 1, 8]
heapq.heapify(nums)            # in place, O(n)
print(nums)                 # 1





"""

Careful: after `heapify`, the list is not sorted. Only `nums[0]` is guaranteed to be the smallest. 
To get items in order, keep calling `heappop`.

Other useful functions instead using heappop for the shorting:
"""

heapq.nsmallest(3, [9, 4, 7, 1, 8])   # [1, 4, 7]
heapq.nlargest(3, [9, 4, 7, 1, 8])    # [9, 8, 7]