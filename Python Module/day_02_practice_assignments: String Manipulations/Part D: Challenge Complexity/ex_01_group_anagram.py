'''
Exercise 11: Group Anagrams
Write a program that starts with a list of strings defined at the top of your script (e.g., words = ["eat", "tea", "tan", "ate", "nat", "bat"]) and groups the anagrams (words formed by rearranging letters) together. Print the final grouped list of lists.

Hardcoded Input: words = ["eat", "tea", "tan", "ate", "nat", "bat"]
Sample Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
'''

# --------------------- Group Anagrams ---------------------

words = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group_anagrams():

    groups = {}

    for word in words:

        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    result = list(groups.values())

    print("Grouped anagrams:", result)


# --------------------- Main ---------------------

def main():
    group_anagrams()


if __name__ == "__main__":
    main()
