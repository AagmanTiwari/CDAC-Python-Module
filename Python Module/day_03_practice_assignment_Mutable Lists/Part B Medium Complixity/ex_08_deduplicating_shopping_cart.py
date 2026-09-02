'''
Exercise 8: De-duplicating Shopping Cart

Scenario: An online shopping cart has duplicate items due to double-clicks: ["apple", "banana", "apple", "orange", "banana", "banana"]. Write a program that processes the list and removes all duplicate items, but keeps the first occurrence of each item in its original order. Print the cleaned cart.

Hardcoded Input: cart = ["apple", "banana", "apple", "orange", "banana", "banana"]
Sample Output: ['apple', 'banana', 'orange']
'''


def main():
    cart = ["apple", "banana", "apple", "orange", "banana", "banana"]

    cleaned_cart = []

    # using list comprehension
    # [cleaned_cart.append(item) for item in cart if item not in cleaned_cart]

    for item in cart:
        if item not in cleaned_cart:
            cleaned_cart.append(item)

    print(cleaned_cart)


main()
