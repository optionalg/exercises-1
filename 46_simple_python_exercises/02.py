"""
    Define a function max_of_three() that takes three
    numbers as arguments and returns the largest of them.
"""


def max_of_three(num1, num2, num3):
    numbers = [num1, num2, num3]
    numbers.sort()
    return numbers[-1]


print(max_of_three(1, 2, 3))
