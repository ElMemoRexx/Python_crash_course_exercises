
# * 5-2. More Conditional Tests:
# You don’t have to limit the number of tests you create to 10.
# If you want to try more comparisons, write more tests and add them
# to conditional_tests.py. Have at least one True and one False result
# for each of the following:

# * Tests for equality and inequality with strings:

# * Testing equality and inequality with strings:
car = 'toyota'
print("Is car == 'toyota'? I predicted True.")
print(car == 'toyota')

car = 'honda'
print("\nIs car != 'honda'? I predicted False.")
print(car != 'honda')

# * Tests using the lower() method:
print("\n    **Testing lower() method:**")
car = 'Subaru'
print("\nIs car.lower() == 'subaru'? I predicted True.")
print(car.lower() == 'subaru')

car = 'Ford'
print("\nIs car.lower() == 'chevrolet'? I predicted False.")
print(car.lower() == 'chevrolet')

# * Numerical tests involving equality and inequality, greater than and
# *  less than, greater than or equal to, and less than or equal to:

print("\n    **Numerical tests:**")
number = 10
print("\nIs number == 10? I predicted True.")
print(number == 10)

number = 5
print("\nIs number != 5? I predicted False.")
print(number != 5)

number = 8
print("\nIs number > 5? I predicted True.")
print(number > 5)

number = 3
print("\nIs number < 3? I predicted False.")
print(number < 3)

number = 7
print("\nIs number >= 7? I predicted True.")
print(number >= 7)

number = 6
print("\nIs number <= 6? I predicted True.")
print(number <= 6)

# * Tests using the and keyword and the or keyword:
print("\n    **Testing 'and' and 'or' keywords:**")
age = 25
has_license = True
print("\nIs age > 18 and has_license == True? I predicted True.")
print(age > 18 and has_license == True)

age = 16
has_license = False
print("\nIs age > 18 or has_license == True? I predicted False.")
print(age > 18 or has_license == True)

# * Test whether an item is in a list:
print("\n    **Testing item in a list:**")
fruits = ['apple', 'banana', 'cherry']
print("\nIs 'banana' in fruits? I predicted True.")
print('banana' in fruits)
print("\nIs 'orange' in fruits? I predicted False.")
print('orange' in fruits)

# * Test whether an item is not in a list:
print("\n    **Testing item not in a list:**")
fruits = ['apple', 'banana', 'cherry']
print("\nIs 'grape' not in fruits? I predicted True.")
print('grape' not in fruits)
print("\nIs 'apple' not in fruits? I predicted False.")
print('apple' not in fruits)
