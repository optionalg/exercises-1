"""
    Define a function max() that takes two numbers
    as arguments and returns the largest of them.
    Use the if-then-else construct available in Python.
    (It is true that Python has the max() function
    built in, but writing it yourself is nevertheless
    a good exercise.)
"""


def max_num(num1, num2):
    if num1 > num2:
        largest = num1
    else:
        largest = num2
    return largest


print(max_num(3, 6))
