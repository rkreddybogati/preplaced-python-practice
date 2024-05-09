

"""
Challenge 3: Coding Challenge
Let's put your understanding into practice with a simple coding challenge.

Task: Write a Python function manage_memory that simulates memory allocation and deallocation. 

The function should:
Take a list of operations where each operation is either 'allocate' or 'deallocate'.

Return the number of memory blocks allocated after all operations are performed, 
assuming each 'allocate' operation adds 1 to the memory block count and each 'deallocate' operation subtracts 1.

Example input: 
            ["allocate", "allocate", "deallocate", "allocate"] Example output: 2

This is a simplified simulation to understand the concept of managing memory.
"""

def manage_memory(operations):
    memory_blocks = 0
    for operation in operations:
        if operation == "allocate":
            memory_blocks += 1
        elif operation == "deallocate":
            memory_blocks -= 1
    return memory_blocks

# Test the function
operations = ["allocate", "allocate", "deallocate", "allocate"]
print(manage_memory(operations))