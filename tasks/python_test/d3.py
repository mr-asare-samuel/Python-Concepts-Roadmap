
# words = ["banana", "kiwi", "apple", "kiwi"]

# unique_words = set(words)

# list_length = [len(n) for n in words]

# unique_words_length = [len(n) for n in unique_words]

# list_tuple = dict(zip(unique_words, unique_words_length))

# print(unique_words)
# print(list_length)
# print(list_tuple)



words = ["banana", "kiwi", "apple", "kiwi"]

unique_words = set(words)
lengths = [len(w) for w in words]
word_lengths = {w: len(w) for w in words}

print(unique_words)
print(lengths)
print(word_lengths)