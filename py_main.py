"""
Write a function, top_three, that takes a list as its argument,
and returns a list of the three largest elements.
For example, top_three([2,3,5,6,8,4,2,1]) == [8, 6, 5]
"""
def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    #implement this function
    return sorted(input_list, reverse=True)[:3]

print(top_three([1, 2]))

print(top_three([2,3,5,6,8,4,2,1]))
