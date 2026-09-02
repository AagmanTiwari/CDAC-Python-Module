"""
Exercise 3: Email Domain Extractor
Write a program that prompts the user to enter an email address string. Extract the domain name (the part after the @) and print it. If the string is not a valid email (does not contain exactly one @), print "Invalid Email".

Sample Input: "vinod@vinod.co"
Sample Output: "vinod.co"

Sample Input: "vinod.co"
Sample Output: "Invalid Email"
"""


def main():
    while True:
        email = input(
            "Enter an email address (or type 'exit' or 'quit' to quit): ").strip()

        if email.lower() in ['exit', 'quit']:
            print("Exiting ....")
            break

        if email.count('@') != 1:
            print("Invalid Email")
            continue

        print(f"Domain: {email.split('@')[1]}")


print("--" * 30)
main()
