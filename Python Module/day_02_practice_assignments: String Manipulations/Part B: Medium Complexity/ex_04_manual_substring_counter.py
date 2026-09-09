'''
Exercise 7: Manual Substring Counter
Write a program that prompts the user to enter a main text string and a substring. Count how many times the substring appears in the main string without using Python's built-in .count() method.

Sample Input: (User inputs main string "banana" and substring "an")
Sample Output: 2
'''

# --------------------- Manual Substring Counter ---------------------


def substring_counter():

    main_text = input("Enter the main text: ")
    substring = input("Enter the substring: ")

    count = 0

    for i in range(len(main_text) - len(substring) + 1):

        if main_text[i:i + len(substring)] == substring:
            count += 1

    print("Substring appears:", count, "times")


# --------------------- Main ---------------------

def main():
    substring_counter()


if __name__ == "__main__":
    main()
