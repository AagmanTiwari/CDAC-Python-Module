"""Exercise 6: Sum of N Natural Numbers
Write a script that accepts a positive integer `N` from the user and calculates the sum of all natural numbers up to `N`.

Sample Input: N = 10
Sample Output: Sum: 55
"""


def main():
    # we do not need to strip whitespace from the input since we are converting it to an integer
    N = int(input("Enter a positive integer N: "))

    print(f'sum : {N * (N + 1) // 2}')


print("--" * 30)
main()


