"""
Exercise 1: Sentence Analysis (Character & Word Count)
Write a Python program that prompts the user to enter a sentence. The program must count and display:

The total number of characters (including spaces and punctuation).
The total number of words.

Sample Input: "Learning Python is fun!"
Sample Output:
Total Characters: 23
Total Words: 4
"""


def main():

    while True:
        sentence = input("Enter a sentence: ").strip()

        if sentence.lower() in ['stop', 'exit', 'enter', 'quit']:
            print("Exiting ....")
            break

        if sentence.strip() == "":
            print("Please enter a vaid sentence")
            continue

        total_characters = len(sentence)
        total_words = len(sentence.split())

        print(f"Total Characters:, {total_characters}")
        print(f"Total Words:, {total_words}")


print("--" * 30)
main()
