"""
    Write a function that takes a character (i.e. a string
    of length 1) and returns True if it is a vowel,
    False otherwise.
"""


def check_vowel(character):
    vowels = ("A", "E", "I", "O", "U", "Y")
    if character in vowels:
        return True
    else:
        return False


print(check_vowel("a".upper()))
