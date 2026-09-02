""" 
Write a program that checks whether a positive integer entered by the user is a prime number.

Logic: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

Sample Input: 17
Sample Output: 17 is a prime number.

"""


def is_prime():
    n = int(input("Enter a positive number: "))

    if n < 2:
        print(f'{n} is not a prime number.')
        return

    limit = n // 2
    for d in range(2, limit + 1):
        if n % d == 0:
            print(f'{n} is not a prime number.')
            break
    else:
        print(f'{n} is a prime number.')


is_prime()
