numbers = [3,3,2,34,5,232,23,2,2,4,23,23,5]

# dedupe first, THEN sort -- a set has no order, so sorting before
# deduping throws that order away anyway.
unique_sorted_numbers = sorted(set(numbers))


print(unique_sorted_numbers)


class Search:
    """
    Binary search only works on SORTED data.

    Idea: keep a `start` and `end` INDEX marking the slice of the list
    that could still contain the target. Each step checks the middle
    index of that slice:
      - middle value == target        -> found, return its index
      - middle value  < target        -> target must be to the right,
                                          so move `start` just past mid
      - middle value  > target        -> target must be to the left,
                                          so move `end` just before mid
    Keep shrinking the slice until it's empty (start > end) or you
    find the target. Each step throws away half the remaining data,
    so this is O(log n) instead of the O(n) of a linear scan.
    """

    def __init__(self):
        self.start = None
        self.end = None

    def find_value(self, data, target_value):
        self.start = 0
        self.end = len(data) - 1

        while self.start <= self.end:
            mid = (self.start + self.end) // 2

            if data[mid] == target_value:
                return mid
            elif data[mid] < target_value:
                self.start = mid + 1
            else:
                self.end = mid - 1

        return -1   # not found


ss = Search()
result_index = ss.find_value(unique_sorted_numbers, 23)
print(result_index)