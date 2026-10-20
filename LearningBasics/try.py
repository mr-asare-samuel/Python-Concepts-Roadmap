
# SECTION 1: FOR LOOPS AND ENUMERATE

# ==========================================

# Loop through each character in a string.

# The variable `ch` holds one character at a time.

for ch in "abc":
    print(ch)

# Use enumerate() to get both the index and the character.

# The index starts at 0 by default.

for i, ch in enumerate("abc"):
    print(i, ch)

# ==========================================

# SECTION 2: STRING ENCODING

# ==========================================

# UTF-8 encoding:

# The word "café" contains the character "é".

# Encoding the string converts it into bytes.

# In UTF-8, "é" is represented by the bytes \xc3\xa9.

print("café".encode("utf-8")) # b'caf\xc3\xa9'

# ==========================================

# SECTION 3: RAW STRINGS

# ==========================================

# A raw string uses the prefix r.

# Backslashes are treated literally instead of introducing

# escape sequences such as \n (newline).

print(r"c:/documents\new")

# ==========================================

# SECTION 4: F-STRINGS

# ==========================================

# F-strings allow variables and expressions to be embedded

# directly inside strings using curly braces.

name = "Alice"
age = 30

print(f"Hello, {name}! You are {age} years old.")

# ==========================================

# SECTION 5: NONE AND CONDITIONAL CHECKS

# ==========================================

# None represents the absence of a value.

name = None

# An if statement checks whether a value is truthy.

# Since name is None, the else block executes.

if name:
    print(f"Hello, {name}!")
else:
    print("Name is not set")

# ==========================================

# SECTION 6: TRUTHY AND FALSY VALUES

# ==========================================

# TRUTHY VALUES:

# - Non-empty strings, e.g. "Hello"

# - Non-zero numbers, e.g. 10 or -5

# - Non-empty lists, e.g. [1, 2]

# - Non-empty dictionaries, e.g. {"name": "Alice"}

# - Non-empty sets, e.g. {1, 2}

# - Non-empty tuples, e.g. (1, 2)

# - True

# FALSY VALUES:

# - Empty strings: ""

# - Zero: 0

# - None

# - Empty lists: []

# - Empty dictionaries: {}

# - Empty sets: set()

# - Empty tuples: ()

# - False

# ==========================================

# SECTION 7: LISTS AND LOOPING THROUGH ELEMENTS

# ==========================================

# Create a list of chemical element names.

elements = [
"sodium", "oxygen", "helium", "carbon", "fluorine",
"chlorine", "bromine", "iodine", "astatine", "radon"
]

# Print each element in the list.

for element in elements:
    print(element)

# Print each element alongside its index.

for i, element in enumerate(elements):
    print(i, element)

# ==========================================

# SECTION 8: APPENDING ITEMS TO A LIST

# ==========================================

# append() adds one item to the end of a list.

elements.append("lead")
elements.append("polonium")
elements.append("astatine")
elements.append("radon")
elements.append("francium")
elements.append("radium")
elements.append("actinium")
elements.append("thorium")
elements.append("protactinium")

# Note: append() allows duplicate values.

# Astatine and radon were already in the original list.

# ==========================================

# SECTION 9: CHECKING LIST MEMBERSHIP

# ==========================================

# The `in` operator checks whether an item exists in a list.

# Python string comparisons are case-sensitive.

# The list contains "chlorine", not "Chlorine".

if "Chlorine" in elements:
    print("Chlorine is in the list")
else:
    print("Chlorine is not in the list")

# The `not in` operator checks whether an item is absent.

# The list contains "helium", not "Helium".

if "Helium" not in elements:
    print("Helium is not in the list")
else:
    print("Helium is in the list")

# ==========================================

# SECTION 10: NUMBER FORMATTING

# ==========================================

# The :.2f format specifier displays a number

# with exactly two digits after the decimal point.

price = 1000000

print(f"The price is {price:.2f} dollars")

# Output: The price is 1000000.00 dollars

# ==========================================

# SECTION 11: STRING LENGTH AND SLICING

# ==========================================

word = "Samuel"

# len() returns the number of characters in a string.

print(f"The length of the word is {len(word)}")

# [::-1] reverses the string.

print(word[::-1])

# ==========================================

# SECTION 12: COPYING AND COMPARING STRINGS

# ==========================================

# Strings are immutable, so slicing creates another string

# with the same contents.

word2 = word[:]

# Reassign word2 to a different string.

word2 = "Samuel12"

# == checks whether the strings have the same contents.

if word == word2:
    print("The words are the same")
else:
    print("The words are not the same")

# ==========================================

# SECTION 13: STRING SLICING TECHNIQUES

# ==========================================

# General slicing syntax:

# string[start\:stop\:step]

#

# start: index where slicing begins

# stop: index where slicing ends (excluded)

# step: number of positions to move each time

# Get the last three characters.

print(word[-3:])

# Get every character except the last three.

print(word[:-3])

# Reverse the string.

print(word[::-1])

# Get every second character, starting at index 0.

print(word[::2])

# Get every second character, starting at index 1.

print(word[1::2])

# Move backwards by two positions at a time.

print(word[::-2])

# Move backwards by three positions at a time.

print(word[::-3])

# Move backwards by four positions at a time.

print(word[::-4])

# Move backwards by five positions at a time.

print(word[::-5])

# Move backwards by six positions at a time.

print(word[::-6])

# ==========================================

# SECTION 14: CONDITIONAL STATEMENTS

# ==========================================

# An if statement executes a block when its condition is true.

# Example 1: Check whether a list contains items.

items = []

if items:
    print("Has items")
else:
    print("Empty") # This runs because the list is empty.

# ==========================================

# SECTION 15: LOGICAL OPERATORS

# ==========================================

age = 25
has_id = True

# AND: Both conditions must be true.

if age >= 18 and has_id:
    print("Allowed")

# OR: At least one condition must be true.

if age < 13 or age > 65:
    print("Discount")

# NOT: Reverses a Boolean condition.

if not has_id:
    print("Show ID")

# ==========================================

# SECTION 16: TERNARY CONDITIONAL EXPRESSION

# ==========================================

# A ternary expression chooses between two values

# based on a condition.

#

# Syntax:

# value_if_true if condition else value_if_false

status = "Adult" if age >= 18 else "Minor"

print(status)

# ==========================================

# SECTION 17: MATCH-CASE STATEMENTS

# ==========================================

# match-case compares a value against different patterns.

# It is available in Python 3.10 and later.

# Use a guard (`if`) to add a condition to a case.

match age:
    case n if n < 13:
        print("Child")
    case n if n < 20:
        print("Teen")
    case _:
        print("Adult")


# ==========================================

# SECTION 18: MATCHING DICTIONARY PATTERNS

# ==========================================

# A dictionary can be matched by its keys and values.

event = {"type": "click", "x": 10, "y": 20}

match event:
    case {"type": "click", "x": x, "y": y}:
        print(f"Click at {x}, {y}")
    case {"type": "key", "key": k}:
        print(f"Key pressed: {k}")
    case _:
        print("Unknown event")


# ==========================================

# SECTION 19: MATCHING A DIFFERENT EVENT

# ==========================================

# This time, the event represents a keyboard action.

event = {"type": "key", "key": "Enter"}

match event:
    case {"type": "click", "x": x, "y": y}:
        print(f"Click at {x}, {y}")
    case {"type": "key", "key": k}:
        print(f"Key pressed: {k}")
    case _:
        print("Unknown event")


# ==========================================

# SECTION 20: USING MATCH-CASE IN A FUNCTION

# ==========================================

# Define a function that accepts an event dictionary.

# The match statement determines how to handle the event.

def handle(event):
    match event:
        case {"type": "click", "x": x, "y": y}:
            print(f"Click at {x}, {y}")
        case {"type": "key", "key": k}:
            print(f"Key pressed: {k}")
        case _:
            print("Unknown event")


# Test the function with different event types.

handle({"type": "click", "x": 5, "y": 8})
handle({"type": "key", "key": "A"})
handle({"type": "scroll"})

# ==========================================

# SECTION 21: MATCHING TUPLES AND COORDINATES

# ==========================================

# A point is represented by a tuple: (x, y).

point = (10, 0)

match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"On x-axis at {x}")
    case (x, y):
        print(f"Point at {x}, {y}")



numbers = [34,5,62,342,53]
numbers.sort()
print(numbers) # does not return the sorted, it works on the list directly

print(sorted(numbers)) # returns the sorted list