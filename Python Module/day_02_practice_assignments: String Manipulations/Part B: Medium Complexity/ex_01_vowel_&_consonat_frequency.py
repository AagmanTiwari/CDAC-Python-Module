"""
Exercise 4: Vowel & Consonant Frequency
Write a program that prompts the user to enter a string and counts:

The individual frequency of each vowel (a, e, i, o, u), case-insensitively.
The total count of all consonants.
Sample Input: "Vinod Kumar Kayartaya"
Sample Output:
Vowel Frequencies:
a: 4
e: 0
i: 1
o: 1
u: 1
Total Consonants: 12
"""


def main():
    user_input = input('Enter a string: ')

    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    total_consonant = 0

    for char in user_input.lower():
        if char in vowels:
            vowels[char] += 1
        elif char.isalpha():
            total_consonant += 1

    for vowel, count in vowels.items():
        print(f"{vowel}: {count}")
    print(f"Total Consonants: {total_consonant}")


main()
