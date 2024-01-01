help(round)


#functions

def perform_operations(a, b): 
    """Well, this is a docstring"""
    subtract = (a - b)
    addition = (a + b)
    division = (a / b)
    return (subtract, addition, division)

print(perform_operations(2, 7))
help(perform_operations)

def make_sense(a, b):
    print(a, b)

make_sense(2,3)

