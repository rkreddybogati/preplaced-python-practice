

# Python is a dynamically typed language
# Let's demonstrate dynamic typing with a simple function

def demonstrate_dynamic_typing(value):
    # Your task is to print the type of the value passed into this function
    print(type(value))

    # Then, reassign a different type of value to the variable and print its type again
    value  = 10.10
    print(type(value))

    pass

# Example usage:
demonstrate_dynamic_typing(10)
# This should print the initial type of 'value', then the new type after reassignment