# Sort() Method
# * Sort() Method
'''The sort() method changes the order of the list permanently. The cars
are now in alphabetical order, and we can never revert to the original order:'''

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# Expected output : ['audi', 'bmw', 'subaru', 'toyota']

# * Reverse() Method
'''The reverse() method changes the order of the list permanently. The cars
are now in reverse alphabetical order, and we can never revert to the original order:'''

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)


# *Sorting a List Temporarily with the sorted() Function
'''To maintain the original order of a list but present it in a sorted order, you
can use the sorted() function. The sorted() function lets you display your list
in a particular order, but doesn't affect the actual order of the list.
Let's try this function on the list of cars.'''

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# * Printing a List in Reverse Order
'''To reverse the original order of a list, you can use the reverse() method. If
we originally stored the list of cars in chronological order according to when
we owned them, we could easily rearrange the list into reverse-chronological
order:'''

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# * Finding the Length of a List
'''You can quickly find the length of a list by using the len() function. The list
in this example has four items, so its length is 4'''
print(len(cars))
