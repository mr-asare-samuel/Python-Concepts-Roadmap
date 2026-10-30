
# ============================================================
# sys: the interpreter
# ============================================================

import sys

"""

print(sys.argv)   # command line argument
print("                ")
print(sys.argv[0])   # get the first items in the list
print("                ")
print(sys.path)
print("                ")
print(sys.platform)
print("                ")
print(sys.version)
print("                ")
print(sys.modules)
print("                ")
print(sys.stdin)
print("                ")
print(sys.stdout)
print("                ")
print(sys.stderr)

"""


# ============================================================
# os: the operating system
# ============================================================

import os

"""

os.getcwd()                    # current working directory
os.listdir(".")                # names in a folder
os.mkdir("data")               # make one folder
os.makedirs("a/b/c", exist_ok=True)   # make nested folders
os.remove("file.txt")          # delete a file. will get this FileNotFoundError: [Errno 2] No such file or directory: 'file.txt' if the file is not found
os.rename("old.txt", "new.txt")


# there is a lot of modules with the os
"""


# ============================================================
# math
# ============================================================

import math

"""
print(math.floor(3.8))
print(math.gcd(12, 18))
print(math.trunc(-3.9))
print(math.isclose(0.1 + 0.2, 0.3))
"""

print(math.pi, math.e)                        # 3.14159..., 2.71828...
print(math.sqrt(16))                          # 4.0
print(math.ceil(3.2))                         # 4   (round up)
print(math.floor(3.8))                        # 3   (round down)
print(math.trunc(-3.9))                       # -3  (cut the decimal)
print(math.factorial(5))                      # 120
print(math.gcd(12, 18))                       # 6
print(math.pow(2, 3))                         # 8.0 (always a float)
print(math.log(8, 2))                         # 3.0
print(math.isclose(0.1 + 0.2, 0.3))           # True
print(math.inf)                               # Infinity


# ============================================================
# datetime
# ============================================================

from datetime import datetime, date, timedelta, timezone

now = datetime.now()                    # current date and time
today = date.today()                    # current date only

d = datetime(2026, 10, 29, 23, 23)
d.year, d.month, d.day                  # 2026, 10, 29
d.hour, d.minute                        # 23, 23
d.weekday()                             # 0 = Monday ... 6 = Sunday


d.strftime("%d %B %Y, %H:%M")    # '29 October 2026, 23:23'
d.strftime("%A")                 # 'Thursday'
d.isoformat()                    # '2026-10-29T23:23:00'


datetime.strptime("2026-10-29", "%Y-%m-%d")
# datetime.datetime(2026, 10, 29, 0, 0)


datetime.now(timezone.utc)


import time

start = time.perf_counter()
# ... work ...
print(time.perf_counter() - start)


# ============================================================
# random
# ============================================================

import random

random.seed(1)         # fixes the sequence, so results repeat (good for tests)

print(random.random())                        # float from 0.0 up to (not including) 1.0
print(random.randint(1, 10))                  # whole number from 1 to 10, both ends included
print(random.uniform(1, 2))                   # float between 1 and 2
print(random.choice(["a", "b", "c"]))         # one random item

items = ["a", "b", "c"]
print(random.choices(items, k=3))             # 3 items, WITH repeats
print(random.sample(range(10), 3))            # 3 unique items, NO repeats

my_list = [1, 2, 3, 4, 5]
print(random.shuffle(my_list))                # None -- shuffles my_list in place
print(my_list)                                # the shuffled list itself


# ============================================================
# re: regular expressions
# ============================================================

import re

text = "call 555-1234 or 555-5678"
pattern = r"\d{3}-\d{4}"

print(re.search(pattern, text))               # first match anywhere, or None -> <re.Match object; span=(5, 13), match='555-1234'>
print(re.match(pattern, text))                # match only at the start -> None (text starts with "call", not a digit)
print(re.fullmatch(pattern, "555-1234"))      # the whole string must match -> <re.Match object; span=(0, 8), match='555-1234'>
print(re.findall(pattern, text))              # list of all matches -> ['555-1234', '555-5678']
print(re.sub(pattern, "[number]", text))      # replace matches -> 'call [number] or [number]'
print(re.split(pattern, text))                # split on matches -> ['call ', ' or ', '']

compiled = re.compile(pattern)                # prepare a pattern to reuse without recompiling each call
print(compiled.findall(text))                 # ['555-1234', '555-5678']


m = re.search(r"\d+", "order 4521 shipped")
m.group()                                  # '4521'

re.findall(r"\d+", "a1b22c333")            # ['1', '22', '333']
re.sub(r"\s+", " ", "a   b    c")          # 'a b c'
re.split(r"[,;]", "a,b;c")                 # ['a', 'b', 'c']


### Groups

# Brackets capture parts of a match:

m = re.search(r"(\w+)@(\w+)\.com", "sam@gmail.com")
m.group(1)       # 'sam'
m.group(2)       # 'gmail'
m.groups()       # ('sam', 'gmail')


# ============================================================
# itertools: tools for iterating
# ============================================================

import itertools

from itertools import (
    chain, islice, count, cycle, repeat, accumulate,
    permutations, combinations, product, groupby, zip_longest,
)

print(list(chain([1, 2], [3, 4])))                         # join iterables end to end -> [1, 2, 3, 4]
print(list(islice(range(100), 5)))                         # first 5 items of any iterable -> [0, 1, 2, 3, 4]
print(list(islice(count(10), 3)))                           # count(10) counts forever -> sliced to [10, 11, 12]
print(list(islice(cycle(["a", "b"]), 4)))                   # cycle repeats forever -> sliced to ['a', 'b', 'a', 'b']
print(list(repeat(7, 3)))                                   # repeats 7, 3 times -> [7, 7, 7]
print(list(accumulate([1, 2, 3, 4])))                       # running totals -> [1, 3, 6, 10]
print(list(permutations([1, 2, 3], 2)))                     # ordered arrangements -> [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]
print(list(combinations([1, 2, 3], 2)))                     # unordered selections -> [(1,2),(1,3),(2,3)]
print(list(product([1, 2], ["a", "b"])))                    # every pairing (nested loops) -> [(1,'a'),(1,'b'),(2,'a'),(2,'b')]
print([(k, list(g)) for k, g in groupby([1, 1, 2, 2, 1])])  # groups CONSECUTIVE equal items -> [(1,[1,1]),(2,[2,2]),(1,[1])]
print(list(zip_longest([1, 2, 3], ["a", "b"], fillvalue="-")))  # like zip, doesn't stop early -> [(1,'a'),(2,'b'),(3,'-')]


list(itertools.chain([1, 2], [3, 4]))              # [1, 2, 3, 4]
list(itertools.islice(itertools.count(10), 3))     # [10, 11, 12]
list(itertools.accumulate([1, 2, 3, 4]))           # [1, 3, 6, 10]

list(itertools.permutations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

list(itertools.combinations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 3)]

list(itertools.product("ab", [1, 2]))
# [('a', 1), ('a', 2), ('b', 1), ('b', 2)]

[(k, list(g)) for k, g in itertools.groupby("aabbbc")]
# [('a', ['a', 'a']), ('b', ['b', 'b', 'b']), ('c', ['c'])]


# ============================================================
# Other standard library modules worth knowing
# ============================================================


# ------------------------------------------------------------
# json: convert between Python dicts/lists and JSON text
# ------------------------------------------------------------

import json

data = {"a": 1, "b": [1, 2]}
text = json.dumps(data)
print(text)                    # '{"a": 1, "b": [1, 2]}'
print(json.loads(text))        # back to a dict -> {'a': 1, 'b': [1, 2]}


# ------------------------------------------------------------
# collections: Counter, defaultdict, deque, namedtuple
# ------------------------------------------------------------

from collections import Counter, defaultdict, deque, namedtuple

print(Counter("aabbbc"))                    # count occurrences -> Counter({'b': 3, 'a': 2, 'c': 1})

dd = defaultdict(int)
dd["x"] += 1                                 # no KeyError on a missing key -- it defaults to int() == 0 first
print(dd)                                    # defaultdict(<class 'int'>, {'x': 1})

dq = deque([1, 2, 3])
dq.appendleft(0)                             # O(1) at either end, unlike a list's insert(0, ...)
dq.appendleft(8)
print(dq)                                    # deque([0, 1, 2, 3])
dq.pop()
print(dq)

Point = namedtuple("Point", ["x", "y"])
print(Point(1, 2))                           # Point(x=1, y=2) -- a tuple with named fields


# ------------------------------------------------------------
# functools: lru_cache, reduce, partial, wraps
# ------------------------------------------------------------

from functools import reduce, partial, lru_cache

print(reduce(lambda a, b: a + b, [1, 2, 3, 4]))   # 10 -- collapses the list to one running total

add = lambda a, b: a + b
add5 = partial(add, 5)                             # pre-fills the first argument
print(add5(3))                                     # 8

@lru_cache
def slow_square(n):
    return n * n

print(slow_square(9), slow_square(9))              # 81 81 -- second call is served from the cache


# ------------------------------------------------------------
# pathlib: object-style file paths
# ------------------------------------------------------------

from pathlib import Path

p = Path("modules/built_ins.py")
print(p.name, p.suffix, p.exists())          # 'built_ins.py' '.py' True


# ------------------------------------------------------------
# time: sleeping, timing, timestamps
# ------------------------------------------------------------

time.sleep(0.01)                             # pause execution for 0.01 seconds
print(time.time())                           # current Unix timestamp (seconds since 1970-01-01)


# ------------------------------------------------------------
# copy: copy, deepcopy
# ------------------------------------------------------------

import copy

original = [1, [2, 3]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)
shallow[1][0] = 99                           # mutates the inner list -- shallow copy shares it with original
print(original, shallow, deep)               # [1, [99, 3]] [1, [99, 3]] [1, [2, 3]]


# ------------------------------------------------------------
# heapq / bisect: heaps, and binary search on sorted lists
# ------------------------------------------------------------

import heapq
import bisect

h = [5, 1, 8, 3]
heapq.heapify(h)
print(heapq.heappop(h))                      # 1 -- always pops the smallest

sorted_list = [1, 3, 5, 7, 9]
print(bisect.bisect(sorted_list, 4))         # 2 -- index to insert 4 and keep the list sorted


# ------------------------------------------------------------
# statistics: mean, median, stdev
# ------------------------------------------------------------

import statistics

nums = [1, 2, 3, 4, 5]
print(statistics.mean(nums), statistics.median(nums), statistics.stdev(nums))


# ------------------------------------------------------------
# csv: read and write CSV files
# ------------------------------------------------------------

import csv
import io

buf = io.StringIO()                          # an in-memory file, so this doesn't touch the filesystem
writer = csv.writer(buf)
writer.writerow(["name", "age"])
writer.writerow(["Ama", 22])
print(buf.getvalue())                        # 'name,age\r\nAma,22\r\n'

buf.seek(0)
print(list(csv.reader(buf)))                 # [['name', 'age'], ['Ama', '22']]


# ------------------------------------------------------------
# logging: proper logs instead of print
# ------------------------------------------------------------

import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logging.info("this goes through logging, not print")   # INFO: this goes through logging, not print


# ------------------------------------------------------------
# argparse: command-line options and help text
# ------------------------------------------------------------

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", default="world")
args = parser.parse_args([])                 # [] -> use the defaults instead of reading real CLI args
print(f"hello {args.name}")                  # hello world


# ------------------------------------------------------------
# typing: type hints
# ------------------------------------------------------------

from typing import List

def total(nums: List[int]) -> int:
    return sum(nums)

print(total([1, 2, 3]))                      # 6 -- the hints don't affect runtime, just tooling/readability


# ------------------------------------------------------------
# dataclasses: classes with less boilerplate
# ------------------------------------------------------------

from dataclasses import dataclass

@dataclass
class DataPoint:
    x: int
    y: int

print(DataPoint(1, 2))                       # DataPoint(x=1, y=2) -- __init__ and __repr__ written for you


# ------------------------------------------------------------
# enum: named constants
# ------------------------------------------------------------

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2

print(Color.RED, Color.RED.value)            # Color.RED 1


# ------------------------------------------------------------
# uuid: unique IDs
# ------------------------------------------------------------

import uuid

print(uuid.uuid4())                          # a random unique id -- different every run


# ------------------------------------------------------------
# hashlib: hashes (SHA-256 and so on)
# ------------------------------------------------------------

import hashlib

print(hashlib.sha256(b"hello").hexdigest())


# ------------------------------------------------------------
# secrets: secure random values
# ------------------------------------------------------------

import secrets

"""
random's output is predictable if you know the seed (random.seed(1) above
proved that -- same seed, same sequence, every time). That's fine for
games, simulations, shuffling a quiz. It's NOT fine for anything security
related -- passwords, API keys, session tokens, password-reset links --
because an attacker who can guess or observe enough of the sequence could
predict the rest. secrets draws from the OS's cryptographic random source
instead, so it's unpredictable even if you know every other value it's
produced.
"""

print(secrets.token_hex(8))                  # random hex string, e.g. for an API key -> 'f3a9c1...' (16 hex chars = 8 bytes)
print(secrets.token_urlsafe(8))              # URL-safe version (base64-ish), e.g. for a password-reset link token
print(secrets.choice(["heads", "tails"]))    # like random.choice, but cryptographically secure
print(secrets.compare_digest("abc123", "abc123"))   # True -- compares in constant time

"""
Why compare_digest and not `==`?  `==` on strings can return faster for an
early mismatching character than a late one -- an attacker measuring that
tiny timing difference over many attempts can slowly guess a secret one
character at a time. compare_digest always takes the same time regardless
of where (or whether) the strings differ, so there's no timing signal to
exploit. Use it whenever you're comparing secrets -- tokens, password
hashes, HMAC signatures -- never plain `==`.
"""


# ------------------------------------------------------------
# subprocess: run other programs
# ------------------------------------------------------------

import subprocess

result = subprocess.run(
    [sys.executable, "-c", "print('hi from a subprocess')"],
    capture_output=True, text=True,
)
print(result.stdout.strip())                 # hi from a subprocess


# ------------------------------------------------------------
# threading / multiprocessing / asyncio: concurrency
# ------------------------------------------------------------

import threading

def worker():
    print("running on a background thread")

t = threading.Thread(target=worker)
t.start()
t.join()


import asyncio

async def say_hello():
    await asyncio.sleep(0.01)
    return "hello from asyncio"

print(asyncio.run(say_hello()))

"""
multiprocessing: not run here on purpose. The default start method
('spawn' on macOS/Windows) re-imports this module in the child process,
so without an `if __name__ == "__main__":` guard around the whole
script, the child would re-run every top-level statement in this file.

import multiprocessing

def square(n):
    return n * n

if __name__ == "__main__":
    with multiprocessing.Pool(2) as pool:
        print(pool.map(square, [1, 2, 3]))
"""


# ------------------------------------------------------------
# unittest: testing
# ------------------------------------------------------------

import unittest

class ExampleTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)

suite = unittest.TestLoader().loadTestsFromTestCase(ExampleTest)
unittest.TextTestRunner(verbosity=0).run(suite)   # avoid unittest.main() -- it reads sys.argv


# ------------------------------------------------------------
# urllib: basic web requests
# ------------------------------------------------------------

from urllib.parse import urlencode, quote

print(urlencode({"q": "hello world", "page": 2}))   # 'q=hello+world&page=2'
print(quote("hello world/safe"))                     # 'hello%20world/safe'
# urllib.request.urlopen(url) makes the actual HTTP call -- not run here
# since it needs network access.


# ------------------------------------------------------------
# sqlite3: a small built-in database
# ------------------------------------------------------------

import sqlite3

conn = sqlite3.connect(":memory:")           # lives only in memory, no file created
cur = conn.cursor()
cur.execute("CREATE TABLE people (name TEXT, age INTEGER)")
cur.execute("INSERT INTO people VALUES (?, ?)", ("Ama", 22))
conn.commit()
cur.execute("SELECT * FROM people")
print(cur.fetchall())                        # [('Ama', 22)]
conn.close()
