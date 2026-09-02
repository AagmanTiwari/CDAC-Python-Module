"""
Exercise 2: Fibonacci Sequence Generator

Write a Python script to print the first 'N' terms of the Fibonacci sequence, where 'N' is provided by the user.

Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

Sample Input: N = 6
Sample Output: 0, 1, 1, 2, 3, 5
"""


def fibonacci_sequence(n):
    a = 0
    b = 1
    for _ in range(n):
        c = a + b
        print(a, end=", ")
        a = b
        b = c


fibonacci_sequence(8)
