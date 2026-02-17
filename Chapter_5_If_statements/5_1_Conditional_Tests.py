
# * 5-1. Conditional Tests:
# Write a series of conditional tests. Print a statement describing each test
# and your prediction for the results of each test. Your code should look
# something like this:

car = 'subaru'
if car == 'subaru':
    print(f"Is {car} == 'subaru'? I predicted True.")
    print(car == 'subaru')

if car != 'audi':
    print(f"\nIs {car} == 'audi'? I predicted False.")
# print("\nIs car == 'audi'? I predicted False.")
    print(car == 'audi')

# *Compared colors
color = 'blue'
print(f"\nIs the color == 'blue'? I predicted True.")
print(color == 'blue')

colors = ['red', 'green', 'blue']
print(f"\nIs 'yellow' in the colors list? I predicted False.")
print('yellow' in colors)

# * compare numbers
number = 10
print(f"\nIs number > 5? I predicted True.")
print(number > 5)

number = 3
print(f"\nIs number < 1? I predicted False.")
print(number < 1)

# * compare using and/or
age = 30
print(f"\nIs age > 18 and age < 40? I predicted True.")
print(age > 18 and age < 40)

age = 50
print(f"\nIs age < 18 or age > 60? I predicted False.")
print(age < 18 or age > 60)

# * test for equality with lower case
name = 'Alice'
print(f"\nIs name.lower() == 'alice'? I predicted True.")
print(name.lower() == 'alice')

name = 'Bob'
print(f"\nIs name.lower() == 'alice'? I predicted False.")
print(name.lower() == 'alice')

# * test for inequality with lower case
fruit = 'Apple'
print(f"\nIs fruit.lower() != 'banana'? I predicted True.")
print(fruit.lower() != 'banana')

fruit = 'banana'
print(f"\nIs fruit.lower() != 'banana'? I predicted False.")
print(fruit.lower() != 'banana')
