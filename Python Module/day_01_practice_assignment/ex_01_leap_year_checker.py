# Exercise 1: Leap Year Checker
"""
01 Write a program that takes a year as input from the user and checks whether it is a leap year or not.

Leap Year Criteria : A year is a leap year if it is divisible by 4, except for century years (ending in 00), which must also be divisible by 400.

Sample Input : `2024`
Sample Output : `2024 is a Leap Year.`

"""


def main():
    # Get user input for the year
    year = int(input("Enter a year: "))

    # Check if the year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a Leap Year.")
    else:
        print(f"{year} is not a Leap Year.")


print("=" * 80)

main()
