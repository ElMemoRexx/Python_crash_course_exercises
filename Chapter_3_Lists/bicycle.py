# This an example of a list
# If we ask Python to print a list, Python return its
# representation of the list, including the brackets.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)


# //*Accessing Elements in a List
# *Lists are ordered collections, so you can access any element in a list by
# *telling Python the position, or index, of the item desired. To access an element in a list, write the name of the list followed by the index of the item
# *enclosed in square brackets."""

# *For example, let’s pull out the first bicycle in the list bicycles:
print(bicycles[0])  # Output: trek

# * We can use the title() method to get a nicely formatted version of the bicycle name.
print(bicycles[0].title())

# * Index Positions Start at 0, Not 1
print(bicycles[1])  # This code returns
print(bicycles[2])  # the second and fourth bicycles in the list

# *'''Python has a special syntax for accessing the last element in a list. If you
# *ask for the item at index -1, Python always returns the last item in the list:'''
print(bicycles[-1])  # Output: specialized


# *Using Individual Values from a List
# this will create a message about the favorite bicycle
# using f-string
message = f"My favorite bicycle is {bicycles[3].title()}."
print(message)
