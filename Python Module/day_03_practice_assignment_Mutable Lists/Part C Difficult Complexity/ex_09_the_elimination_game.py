'''
Exercise 9: The Josephus Elimination Game
Scenario: A group of N soldiers (numbered 1 to N) stand in a circle. Starting from the first soldier, every K-th soldier is eliminated from the circle. The count continues with the next remaining soldier, moving clockwise. This process repeats until only one soldier remains. Write a program that prompts the user to enter N (number of soldiers) and K (elimination interval). Simulate the game using a list and print the order of eliminations and the final survivor.

Sample Input: N = 5, K = 2
Sample Output:
Soldier circle initialized: [1, 2, 3, 4, 5]
Eliminated soldier: 2 (Remaining: [1, 3, 4, 5])
Eliminated soldier: 4 (Remaining: [1, 3, 5])
Eliminated soldier: 1 (Remaining: [3, 5])
Eliminated soldier: 5 (Remaining: [3])
The sole survivor is: 3

'''


def main():
    N = int(input("Enter the number of soldiers (N): "))
    K = int(input("Enter the elimination interval (K): "))
    # Initialize the list of soldiers
    soldiers = list(range(1, N + 1))
    print(f"Soldier circle initialized: {soldiers}")

    # Start from the first soldier
    index = 0

    # Continue until only one soldier remains
    while len(soldiers) > 1:
        # Calculate the index of the soldier to eliminate
        index = (index + K - 1) % len(soldiers)
        eliminated_soldier = soldiers.pop(index)
        print(
            f"Eliminated soldier: {eliminated_soldier} (Remaining: {soldiers})")

    # The last remaining soldier is the survivor
    survivor = soldiers[0]
    print(f"The sole survivor is: {survivor}")


main()
