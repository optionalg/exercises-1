"""
    Define a function sum() and a function multiply()
    that sums and multiplies (respectively) all the
    numbers in a list of numbers. For example,
    sum([1, 2, 3, 4]) should return 10,
    and multiply([1, 2, 3, 4]) should return 24.
"""


def sum_of_numbers():
    add_total = 0
    numbers = [1, 2, 3, 4]
    for i in numbers:
        add_total += i
    return add_total


def sum_of_numbers_multiplied():
    multiply_total = 1
    numbers = [1, 2, 3, 4]
    for i in numbers:
        multiply_total *= i
    return multiply_total


print(sum_of_numbers())
print(sum_of_numbers_multiplied())
