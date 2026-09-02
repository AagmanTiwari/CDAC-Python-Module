'''
Exercise 8: Score to Grade Converter
Write a script that takes a numeric test score from the user (0 to 100) and displays a corresponding letter grade based on the following scale:

90-100: A
80-89: B
70-79: C
60-69: D
Below 60: F
'''


def main():
    test_score = float(input("Enter the test score (0-100): "))

    if 90 <= test_score <= 100:
        grade = 'A'
    elif 80 <= test_score < 90:
        grade = 'B'
    elif 70 <= test_score < 80:
        grade = 'C'
    elif 60 <= test_score < 70:
        grade = 'D'
    elif 0 <= test_score < 60:
        grade = 'F'
    else:
        print("Error: Please enter a valid score between 0 and 100.")
        return

    print(f"Grade: {grade}")


print("--" * 30)
main()
