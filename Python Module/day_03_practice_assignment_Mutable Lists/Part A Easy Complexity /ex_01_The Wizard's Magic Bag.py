'''
Exercise 1: The Wizard's Magic Bag
Scenario: A wizard has a magic bag containing a sequence of items: ["staff", "potion", "spellbook"]. When the wizard steps through a magic portal, two things happen:

A new item enters the bag (prompts the user to input the item name to append to the end).
The oldest item in the bag (at index 0) is dissolved and ejected. Write a program to simulate this portal transition and print the final bag contents.
Sample Input: (User inputs "amulet")
Sample Output:
Portal transition activated!
Ejected oldest item: staff
Current items in the magic bag: ['potion', 'spellbook', 'amulet']
'''


def main():
    magic_bag = ["staff", "potion", "spellbook"]
    while True:
        added_item_in_magic_bag = input("Enter the item: ").strip()

        if added_item_in_magic_bag.lower() == "exit":
            print("Exiting .....")
            break

        if added_item_in_magic_bag == "":
            print("Please enter a valid item name.")
            continue

        print("Portal transition activated!")

        if added_item_in_magic_bag:
            magic_bag.append(added_item_in_magic_bag)

            if len(magic_bag) > 0:
                ejected_item = magic_bag.pop(0)
                print(f"Ejected oldest item: {ejected_item}")
            else:
                print("The magic bag is empty. No item to eject.")

        else:
            print("No item was added to the magic bag.")

        print(f"Current items in the magic bag: {magic_bag}")


main()
