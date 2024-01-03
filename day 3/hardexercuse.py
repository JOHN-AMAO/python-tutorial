#Have you ever felt debugging involved a bit of luck? The following program has a bug. Try to identify the bug and fix it.


"""def has_lucky_number(nums):
    Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    
    for num in nums:
        if num % 7 == 0:
            return True
        else:
            return False
"""

def has_lucky_number(nums):
    return True if any([ num % 7 == 0 for num in nums]) else False

has_lucky_number([2,3,4,5,6,7])

def elementwise_greater_than(L, thresh):

    return [n > thresh for n in L]
elementwise_greater_than([1, 2, 3, 4], 2)