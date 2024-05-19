

"""
Write a function named sum_numbers that takes two parameters: num1 (an integer) and 
num2_str (a string representing a number). 

The function should convert num2_str to either an integer or a float, as appropriate, 
and return the sum of num1 and num2_str as a float.

"""


def sum_numbers(num1, num2_str):
    # Your code here
    return num1+float(num2_str)

# Example usage
print(sum_numbers(5, "10.5"))  # Should print 15.5