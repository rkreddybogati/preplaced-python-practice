
""" 
Challenge 1: 
    Write a Python function that takes a list of numbers and returns a dictionary with two keys, 
    even and odd, with lists as values containing the even and odd numbers, respectively.

For example, 
    given [1, 2, 3, 4, 5], the function should return {'even': [2, 4], 'odd': [1, 3, 5]}.
 """
def classify_numbers(numbers):
    even = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    return {'even': even, 'odd': odd}

# Test your function with a list of numbers
print(classify_numbers([1, 2, 3, 4, 5]))




"""
Challenge 2: 
Create a Python function that takes a dictionary representing a shopping cart and calculates the total price. 
The dictionary keys are item names, and the values are tuples containing the price per item and quantity.

For example, 
    given {"apples": (30, 2), "bananas": (20, 1), "oranges": (50, 3)}, your function should return 230.
"""
def calculate_total(cart):
    total = 0
    for item in cart.values():
        total += item[0] * item[1]

    return total
# Test your function with a shopping cart
print(calculate_total({'apples': (30, 2), 'bananas': (20, 1), 'oranges': (50, 3)}))

