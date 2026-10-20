def min_max(nums):
    return min(nums), max(nums)


low, high = min_max([3, 1, 9, 4])

print(low, high)