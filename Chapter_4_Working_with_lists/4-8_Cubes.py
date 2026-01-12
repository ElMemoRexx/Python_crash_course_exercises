
# *4-8. Cubes:
'''A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube.'''
cubes = [value ** 3 for value in range(1, 11)]
for cube in cubes:
    print(cube)


# Alternative solution using a for loop and append():
cubes = []  # * Create an empty list called cubes
for value in range(1, 11):  # * Loop through numbers from 1 to 10 (11 is not included)
    # * Calculate the cube of each number and add it to the list
    cubes.append(value ** 3)
for cube in cubes:  # * Print each cube value separately
    print(cube)
