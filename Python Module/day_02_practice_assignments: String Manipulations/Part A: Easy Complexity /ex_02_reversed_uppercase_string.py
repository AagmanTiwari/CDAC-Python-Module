"""
Exercise 2: Reversed Uppercased String
Write a program that takes a string input from the user, reverses the string, converts the entire reversed string to uppercase, and prints the result.

Sample Input: "Bangalore"
Sample Output: "EROLAGNAB"
"""


def main():
    while True:
        user_input = input(
            "Enter a string (or type 'exit' or 'quit' to quit): ").strip()

        if user_input.lower() in ['exit', 'quit']:
            print("Exiting ....")
            break

        if user_input == "":
            print("Please enter a valid string.")
            continue

        reversed_string = user_input[::-1].upper()

        print(f"Reversed Uppercased String: {reversed_string}")


print("--" * 30)
main()
