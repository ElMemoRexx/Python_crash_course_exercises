
# *3-8. Seeing the World:
'''Store the locations in a list. Make sure the list is not in alphabetical order'''
places = ["tokyo", "españa", "italia", "londres", "nueva zelanda"]

'''Print your list in its original order. Don't worry about printing the list neatly;
just print it as a raw Python list.'''
print("Original list:")
print(places)

'''Use sorted() to print your list in alphabetical order without modifying the
actual list.'''
print("\nsorted list:")
print(sorted(places))

'''Show that your list is still in its original order by printing it.'''
print("\nOriginal list after sorted():")
print(places)

'''Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.'''
print("\nHere is the reverse-alphabetical list: ")
print(sorted(places, reverse=True))

'''• Show that your list is still in its original order by printing it again.
'''
print("\nHere is the original list again: ")
print(places)

'''Use reverse() to change the order of your list. Print the list to show that its
order has changed'''
places.reverse()
print("\nHere the reverse list: ")
print(places)

# Español

# Vuelve a invertir para regresar al orden original
places.reverse()
print("\nList after second reverse():")
print(places)

# Ordena la lista alfabéticamente de forma permanente
places.sort()
print("\nList after sort():")
print(places)

# Ordena la lista en orden alfabético inverso de forma permanente
places.sort(reverse=True)
print("\nList after sort(reverse=True):")
print(places)
