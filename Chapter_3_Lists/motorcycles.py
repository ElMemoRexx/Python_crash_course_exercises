
# *Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# *Adding Elements to a List
# *Appending Elements to the End of a List
# *append() method adds an element to the end of a list
motorcycles.append('ducati')
print(motorcycles)  # It will be added to the end of the list


'''The append() method makes it easy to build lists dynamically. For example,
you can start with an empty list and then add items to the list using a series
of append() calls. Using an empty list, let's add the elements 'honda', 'yamaha',
and 'suzuki' to the list:'''

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)


# *Inserting Elements into a List
# This will add 'ducati' to the beginning of the list
motorcycles.insert(0, 'ducati')
print(motorcycles)

# *Removing an Item Using the del Statement
del motorcycles[0]  # This will remove the first item from the list
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# *Removing an Item Using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
