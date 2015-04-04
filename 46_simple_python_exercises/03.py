"""
    Define a function that computes the length of
    a given list or string. (It is true that Python
    has the len() function built in, but writing it
    yourself is nevertheless a good exercise.)
"""


def length():
    string = "Python"
    string_length = 0
    for i in string:
        string_length += 1
    return string_length


print(length())
