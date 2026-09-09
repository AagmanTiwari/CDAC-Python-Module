'''
Exercise 8: Name Anonymizer
Write a program that prompts the user to enter a full name (first name, middle name, last name) and anonymizes it. The output should print the initials of the first and middle names followed by the full last name. If the name consists of only a single word, print it as-is.

Sample Input: "Vinod Kumar Kayartaya"
Sample Output: "V. K. Kayartaya"
Sample Input: "Bangalore"
Sample Output: "Bangalore"

'''

# --------------------- Name Anonymizer ---------------------


def anonymize_name():

    full_name = input("Enter your full name: ").strip()

    names = full_name.split()

    if len(names) == 1:
        print(names[0])

    else:
        result = ""

        for i in range(len(names) - 1):
            result += names[i][0].upper() + ". "

        result += names[-1]

        print("Anonymized name:", result)


# --------------------- Main ---------------------

def main():
    anonymize_name()


if __name__ == "__main__":
    main()
