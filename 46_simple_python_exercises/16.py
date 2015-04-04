"""
    Write a function filter_long_words() that takes
    a list of words and an integer n and returns
    the list of words that are longer than n.
"""


def filter_long_words():

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F',
                'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z', " "]

    user_str = input("Type in some text...").upper()
    user_int = int(input("Type in a number"))

    char_list = []
    long_words = []

    for i in user_str:
        if i in alphabet:
            char_list.append(i)

    words = (''.join(char_list))
    words = words.split()

    for j in words:
        if len(j) > user_int:
            long_words.append(j)

    return long_words


print(filter_long_words())
