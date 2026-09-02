'''Exercise 3: The Cargo Train Scanner
Scenario: A train has wagons carrying different resources: 
["coal", "iron", "gold", "coal", "timber", "coal"]. The train conductor wants to inspect the cargo. Write a program that prompts the user to enter a resource type (e.g., "coal" or "gold").

Print the total number of wagons carrying that resource (using .count()).
If the resource is on the train, print the index of the very first wagon carrying it (using .index()). If it is not found, print "Resource not found on train!".

Sample Input: "coal"
Sample Output:
Number of coal wagons: 3
First coal wagon is at index: 0

Sample Input: "oil"
Sample Output: "Resource not found on train!"
'''


def main():
    wagon_carrying_resources = [
        "coal", "iron", "gold", "coal", "timber", "coal"]
    while True:
        resources_to_search = input(
            "Enter the resource type to search (or type 'exit' or 'return' to quit): ").strip().lower()

        if resources_to_search in ["", "exit"]:
            print("Exiting ...")
            break

        if resources_to_search in wagon_carrying_resources:
            count = wagon_carrying_resources.count(resources_to_search)
            index = wagon_carrying_resources.index(resources_to_search)
            print(
                f"Number of {resources_to_search} wagons: {count}\nFirst {resources_to_search} wagon is at index: {index}")

        else:
            print("Resource not found on train!")


main()
