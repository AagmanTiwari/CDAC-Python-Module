'''
Exercise 6: Grading on a Curve

Scenario: A professor wants to adjust exam grades. Prompt the user to enter a list of space-separated test scores. Convert them to a list of integers. Using a single list comprehension with conditionals, apply the following curve rules:

If a score is below 50, add 10 points.
If a score is 50 or higher, add 5 points.
The maximum possible score is capped at 100 (e.g., a score of 98 becomes 100, not 103). Print the original and the curved grades.
Sample Input: "45 88 30 98 50"
Sample Output:
Original: [45, 88, 30, 98, 50]
Curved: [55, 93, 40, 100, 55]
'''


def main():

    scores_input = input("Enter a list of space-separated test scores: ")

    # Convert the input string to a list of integers
    original_scores = [int(score) for score in scores_input.split()]

    max_score = 100  # Define the maximum score

    # Apply the curve using a list comprehension with conditionals
    curved_scores = [min(score + 10, max_score) if score <
                     50 else min(score + 5, max_score) for score in original_scores]

    # Print the original and curved grades
    print(f"Original: {original_scores}")
    print(f"Curved: {curved_scores}")


main()
