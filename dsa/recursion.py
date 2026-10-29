"""
RECURSION — NOTES

What it is:
    A function that solves a problem by calling itself on a smaller
    version of the same problem, until the problem is small enough to
    answer directly.

Every recursive function needs two parts:
    1. Base case  — the smallest version of the problem, answered directly,
                     with NO further recursive call. This is what stops
                     the recursion. Without it, the function calls itself
                     forever and crashes with RecursionError (stack overflow).
    2. Recursive case — breaks the problem into a smaller version of
                     itself, and calls the function again on that smaller
                     piece, then combines the result with something to
                     move toward the base case.

The call stack:
    Each call to the function is placed on top of a stack and waits there
    (paused) until the call it made returns a value. Once the base case
    is hit, calls start returning and popping off the stack from the top
    down, each one finishing the pending `+` (or other work) it was
    waiting on.

Walking through fibonacci(4):
    fibonacci(4)
      -> fibonacci(3) + fibonacci(2)
           fibonacci(3) -> fibonacci(2) + fibonacci(1)
               fibonacci(2) -> fibonacci(1) + fibonacci(0)
                   fibonacci(1) -> 1   (base case)
                   fibonacci(0) -> 0   (base case)
               fibonacci(2) -> 1 + 0 = 1
               fibonacci(1) -> 1       (base case)
           fibonacci(3) -> 1 + 1 = 2
           fibonacci(2) -> 1   (computed again, see note below)
      fibonacci(4) -> 2 + 1 = 3

Key things to notice:
    - Nothing actually loops. Each call either returns immediately
      (base case) or waits on two smaller calls and adds their results.
    - The same sub-problem (e.g. fibonacci(2)) gets solved more than
      once. This naive version is O(2^n) time because of that repeated
      work — it recomputes the same values exponentially many times.
      (Fix: "memoization" — cache results already computed — or switch
      to an iterative/bottom-up approach, both O(n).)
    - Space complexity is O(n) here, because the call stack only ever
      grows as deep as the chain position -> position-1 -> position-2...,
      not as wide as the number of calls made.

Mental model for writing any recursive function:
    1. What is the smallest input I can answer without recursing?
         (the base case)
    2. Assuming a call to this function already correctly solves a
       SMALLER version of the problem, how do I use that to solve the
       current, bigger one?
         (the recursive case — trust the smaller call works)
    3. Does every recursive call move strictly closer to the base case?
         (otherwise: infinite recursion)
"""

# position :   0, 1, 2, 3, 4, 5, 6, 7,  8,  9
# fibonacci:  0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def fibonacci(position):
    if position == 0 or position == 1:
        return position
    return fibonacci(position-1) + fibonacci(position-2)




def sumations(nums):
    if not nums:
        return 0
    return nums[0] + sumations(nums[1:])


print(sumations([2,4,23,12,1]))





"""
Sum of Nested Lists Using Recursion

Write a Python program to sum recursion lists using recursion.

Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 18   (only [3,4] and [5,6] are summed; the top-level
                        1 and 2 are skipped, not nested lists)


"""

def sum_all(data):
    """Sum every number in data, however deeply nested. No skipping --
    once you're inside a nested list, every number in it counts."""
    sum = 0
    for n in data:
        if isinstance(n, list):
            sum = sum + sum_all(n)
        else:
            sum = sum + n
    return sum


def sum_nested(data):
    """Skip top-level plain numbers (1, 2). For each top-level item
    that IS a list, hand it to sum_all so everything inside it counts."""
    sum = 0
    for n in data:
        if isinstance(n, list):
            sum = sum + sum_all(n)
        # else: plain number at the top level -> skip it

    return sum


print(sum_nested([1, 2, [3, 4], [5, 6]]))


if __name__ == "__main__":
    print(fibonacci(7))



def sum_list(data):
    if len(data) == 1:
        return data[0]
    else:
        return data[0] + sum_list(data[1:])
        

print(sum_list([2, 4, 5, 6, 7]))


def factorial(number):
    if number == 1:
        return number
    return number * factorial(number - 1)


print(factorial(5))


def sum_series(n):
    if n < 1:
        return 0

    return n + sum_series(n - 2)

print(sum_series(6))


def sum_even(data_list):
    if len(data_list) == 0:
        return 0

    if data_list[0] % 2 == 0:
        return data_list[0] + sum_even(data_list[1:])

    return sum_even(data_list[1:])


print(sum_even([2, 5, 6]))
        