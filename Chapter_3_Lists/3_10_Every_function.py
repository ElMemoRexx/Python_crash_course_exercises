'''3-10. Every Function: Think of things you could store in a list. For example, you
could make a list of mountains, rivers, countries, cities, languages, or anything
else you'd like. Write a program that creates a list containing these items and
then uses each function introduced in this chapter at least once.'''

# We need to create a list of everything first
# We need to make sure to use each function introduced in this chapter at least once
# The functions introduced in this chapter are:
# * - append()
# * - insert()
# * - remove()
# * - pop()
# * - sorted()
# * - sort()
# * - reverse()
# * - len()


# Let's create a list of countries
countries = ["Japan", "Spain", "Italy", "UK", "New Zealand"]
countries.append("Mexico")  # Adding a city to the list
countries.insert(2, "Canada")  # Inserting a country at index 2
print("After append and insert:", countries)

countries.remove("UK")
print("after removing UK:", countries)

popped_country = countries.pop()
print("After pop:", countries)
print("popped country:", popped_country)

print("Sorted list (temporary):", sorted(countries))  # Temporary sort
countries.sort()  # Permanent sort
print("Sorted list (permanent):", countries)

countries.reverse()  # Reverse the list
print("Reversed list:", countries)

countries.append("Japan")                 # Add a duplicate for count()
print("List with duplicate:", countries)
print("Count of 'Japan':", countries.count("Japan"))  # count()

print("Number of countries:", len(countries))         # len()
