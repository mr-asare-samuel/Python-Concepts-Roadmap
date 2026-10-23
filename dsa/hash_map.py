class HashMap:
    def __init__(self, size=8):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self.count = 0

    def _index(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        bucket = self.buckets[self._index(key)]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)    # update existing key
                return
        bucket.append((key, value))         # new key
        self.count += 1
        if self.count / self.size > 0.75:
            self._resize()

    def get(self, key, default=None):
        bucket = self.buckets[self._index(key)]
        for k, v in bucket:
            if k == key:
                return v
        return default

    def remove(self, key):
        bucket = self.buckets[self._index(key)]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return True
        return False

    def _resize(self):
        old_buckets = self.buckets
        self.size *= 2
        self.buckets = [[] for _ in range(self.size)]
        self.count = 0
        for bucket in old_buckets:
            for k, v in bucket:
                self.put(k, v)


m = HashMap()
m.put("ama", 25)
m.put("kofi", 30)
m.put("ama", 26)           # updates ama

print(m.get("ama"))        # 26
print(m.get("zed", "n/a")) # n/a
m.remove("kofi")
print(m.get("kofi"))       # None

