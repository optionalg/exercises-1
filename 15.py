"""
    Write a function find_longest_word() that takes
    a list of words and returns the length
    of the longest one.
"""


def find_longest_word():
    words_list = ["Python", "programming", "fun"]
    words_len = []
    for i in words_list:
        words_len.append((len(i), i))
    words_len.sort()
    return words_len[-1][1]


print(find_longest_word())
