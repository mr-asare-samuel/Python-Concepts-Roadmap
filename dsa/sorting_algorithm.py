import time
import random


# Bubble Sort: O(n) ......... (Very Slow and simple to learn)...........

def bubble_sort(arr):
    arr = arr[:]                       # work on a copy
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:                # no swaps means already sorted
            break
    return arr




# ### Selection sort: O(n²) .......Idea: Find the smallest item in the unsorted part and swap it to the front. Repeat. .........

def selection_sort(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr



# Insertion sort: O(n)  ......... Like sorting playing cards in your hand. Take the next item and slide it left into the right spot in the already-sorted part.

def insertion_sort(arr):
    arr = arr[:]
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]        # shift bigger items right
            j -= 1
        arr[j + 1] = current           # drop into the gap
    return arr





"""
The fast sorts (O(n log n)) ...............................................
"""

# Merge sort ................. 

"""
Idea:

1. **Split** the list in half, again and again, until each piece has 1 item (a single item is already sorted).
2. **Merge** pairs of sorted pieces back together into bigger sorted pieces.
"""

def merge_sort(arr):
    if len(arr) <= 1:                  # base case
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:        # <= keeps it stable
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])            # one of these is empty
    result.extend(right[j:])
    return result



# Quick sort.............

"""
**Idea:**

1. Pick a **pivot**.
2. Put everything smaller to its left, everything larger to its right.
3. Recursively sort the left and right parts.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)


# Heap sort..............

"""
Idea: Put everything in a min-heap, then pop the smallest repeatedly.
"""

import heapq

def heap_sort(arr):
    h = arr[:]
    heapq.heapify(h)                               # O(n)
    return [heapq.heappop(h) for _ in range(len(h))]   # n pops, O(log n) each




""" Non-comparison sort:  ....................................

Counting sort: O(n + k).... Instead of comparing, count how many times each value appears. Works for whole numbers in a small range.
"""

def counting_sort(arr):
    if not arr:
        return []
    counts = [0] * (max(arr) + 1)
    for n in arr:
        counts[n] += 1
    out = []
    for value, c in enumerate(counts):
        out.extend([value] * c)
    return out

print(counting_sort([4, 2, 2, 8, 3, 3, 1]))    # [1, 2, 2, 3, 3, 4, 8]

















# Prints_______
print("                ")
print("Selection sort", selection_sort([34, 48, 12, 1, 43, 66, 6]))
print("Selection sort", selection_sort([5, 5, 5, 5]))
print("Selection sort", selection_sort([]))
print("Selection sort", selection_sort([1]))
print("Selection sort", selection_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))   # reverse-sorted, worst case for both algorithms

print("                ")
print("bubble sort", bubble_sort([34, 48, 12, 1, 43, 66, 6]))
print("bubble sort", bubble_sort([5, 5, 5, 5]))
print("bubble sort", bubble_sort([]))
print("bubble sort", bubble_sort([1]))
print("bubble sort", bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))   # reverse-sorted, worst case for both algorithms

print("                ")
print("insertion sort", insertion_sort([34, 48, 12, 1, 43, 66, 6]))
print("insertion sort", insertion_sort([5, 5, 5, 5]))
print("insertion sort", insertion_sort([]))
print("insertion sort", insertion_sort([1]))
print("insertion sort", insertion_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))   # reverse-sorted, worst case for both algorithms

print("                ")
print("merge sort", merge_sort([34, 48, 12, 1, 43, 66, 6]))
print("merge sort", merge_sort([5, 5, 5, 5]))
print("merge sort", merge_sort([]))
print("merge sort", merge_sort([1]))
print("merge sort", merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))   # reverse-sorted

print("                ")
print("quick sort", quick_sort([34, 48, 12, 1, 43, 66, 6]))
print("quick sort", quick_sort([5, 5, 5, 5]))
print("quick sort", quick_sort([]))
print("quick sort", quick_sort([1]))
print("quick sort", quick_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))   # reverse-sorted

print("                ")
print("heap sort", heap_sort([34, 48, 12, 1, 43, 66, 6]))
print("heap sort", heap_sort([5, 5, 5, 5]))
print("heap sort", heap_sort([]))
print("heap sort", heap_sort([1]))
print("heap sort", heap_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))   # reverse-sorted

print("                ")
print("counting sort", counting_sort([34, 48, 12, 1, 43, 66, 6]))
print("counting sort", counting_sort([5, 5, 5, 5]))
print("counting sort", counting_sort([]))
print("counting sort", counting_sort([1]))
print("counting sort", counting_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))   # reverse-sorted



# Just for checking the time it takes for a sort to complete

# Timing: how long each one takes on the same data
"""
time.perf_counter() gives a high-resolution clock reading, in seconds.
Call it before and after the work, and subtract -- the difference is how
long that call took to run. perf_counter() is preferred over time.time()
for measuring elapsed time because it's monotonic (never jumps backward,
e.g. from a system clock adjustment) and has a smaller resolution.
"""

def timed(sort_fn, data):
    start = time.perf_counter()
    sort_fn(data)
    end = time.perf_counter()
    return end - start


data = [random.randint(0, 10_000) for _ in range(2000)]

bubble_time = timed(bubble_sort, data)
selection_time = timed(selection_sort, data)
insertion_time = timed(insertion_sort, data)
merge_time = timed(merge_sort, data)
quick_time = timed(quick_sort, data)
heap_time = timed(heap_sort, data)
counting_time = timed(counting_sort, data)

print("                ")
print(f"bubble_sort:    {bubble_time:.6f} sec")
print(f"selection_sort: {selection_time:.6f} sec")
print(f"insertion_sort: {insertion_time:.6f} sec")
print(f"merge_sort:     {merge_time:.6f} sec")
print(f"quick_sort:     {quick_time:.6f} sec")
print(f"heap_sort:      {heap_time:.6f} sec")
print(f"counting_sort:  {counting_time:.6f} sec")




#___--------___________-----------______________------------__________

# Sorting in Python (what you actually use) ...........
# ____ You almost never write your own sort. Python's built-in is faster and well tested.__


nums = [5, 3, 8, 1, 2]

sorted(nums)               # new sorted list, original unchanged
nums.sort()                # sorts in place, returns None
sorted(nums, reverse=True) # descending


"""
Reminder: `nums = nums.sort()` sets `nums` to `None`.

`sorted()` works on **any iterable** (tuple, set, dict keys, string) and always returns a **list**. `.sort()` is a list-only method.
"""


people = [("Ama", 22), ("Kofi", 30), ("Yaw3e", 22)]

print("                ")
print(sorted(people, key=lambda p: (p[1], p[0])))    # by age, then by name