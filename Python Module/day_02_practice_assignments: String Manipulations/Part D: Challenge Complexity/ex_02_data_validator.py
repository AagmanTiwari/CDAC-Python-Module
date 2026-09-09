'''
Exercise 12: Date Validator & Pretty Formatter

Write a program that prompts the user to enter a date string in the format "DD/MM/YYYY".

Warning

Do not use any built-in date/time library functions (such as the datetime or time modules) to format or validate the dates. You must parse and split the string manually, and use a custom tuple of month names for the pretty output if needed.

Your program must:

* Verify if the date is valid. To be valid:
   . The month must be between 1 and 12 inclusive.
   . The day must be valid for that specific month (e.g., April, June, September, November have 30 days; others have 31 days).
   . For February, the day must be at most 29 in a leap year (divisible by 4, except for centuries not divisible by 400) and at most 28 in standard years.

* If the date is valid, use a tuple of month names ("January", "February", ...) to format and print the date in a long-form readable layout: "MonthName DD, YYYY".

* If the date is invalid, print "Invalid Date".

Sample Input: "26/08/2026"
Sample Output: "August 26, 2026"

Sample Input: "29/02/2026" (2026 is not a leap year)
Sample Output: "Invalid Date"

Sample Input: "31/04/2026" (April only has 30 days)
Sample Output: "Invalid Date"
'''

# --------------------- Date Validator & Pretty Formatter ---------------------


def validate_date():

    date = input("Enter date (DD/MM/YYYY): ")

    try:
        parts = date.split("/")

        if len(parts) != 3:
            print("Invalid Date")
            return

        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])

    except ValueError:
        print("Invalid Date")
        return

    month_names = (
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    )

    if month < 1 or month > 12:
        print("Invalid Date")
        return

    if month == 2:

        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            max_days = 29

        else:
            max_days = 28

    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_days = 30

    else:
        max_days = 31

    if day < 1 or day > max_days:
        print("Invalid Date")

    else:
        print(month_names[month - 1], day, ",", year)


# --------------------- Main ---------------------

def main():
    validate_date()


if __name__ == "__main__":
    main()
