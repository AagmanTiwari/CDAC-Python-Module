'''
Exercise 5: The Spy's Word Reverser

Scenario: A secret agent wants to send an encrypted message. The encryption rule is simple: reverse every word in the sentence, but keep the order of words unchanged. Write a program that prompts the user for a sentence, splits it, uses a list comprehension to reverse the letters of each word, and joins them back together.

Sample Input: "Meet me at midnight"
Sample Output: "teeM em ta thgindim"

'''


def main():
    sentence = input("Enter a sentence: ").strip()

    if sentence == "":
        print("Please enter a valid sentence.")
        return

    reversed_words = [word[::-1] for word in sentence.split()]
    encrypted_message = ' '.join(reversed_words)

    print(f"Encrypted message: {encrypted_message}")


main()
