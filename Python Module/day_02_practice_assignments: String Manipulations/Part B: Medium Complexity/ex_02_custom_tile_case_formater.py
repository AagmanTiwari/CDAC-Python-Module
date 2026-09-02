'''
Exercise 5: Custom Title Case Formatter
Write a program that accepts a string input from the user and outputs it in Title Case (capitalizing the first letter of each word and lowercasing the remaining letters). Do not use Python's built-in .title() method.

Sample Input: "WELCOME TO BANGALORE CITY"
Sample Output: "Welcome To Bangalore City"

'''


def main():
    sentence = input("Enter a sentence: ").strip()

    words = sentence.split()

    title_sentence = []

    for word in words:
        # or i can simply use word.capitalize() but as per the instruction we are not using built-in methods
        # title_sentence.append(word.capitalize())
        formatted_word = word[0].upper() + word[1:].lower()
        title_sentence.append(formatted_word)

    result = " ".join(title_sentence)

    print("Title Case:", result)


main()
