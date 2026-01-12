
# *4-9. Cube Comprehension:
'''Use a list comprehension to generate a list of the first
10 cubes.'''
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

# todo: checkpoint page 60 chapter 4
# 1. What is a list comprehension? A concise way to create lists in Python.
# 2. How do you create a list of cubes using a for loop?
# 3. What are the benefits of using a list comprehension over a for loop?
# 4. Can you create a list of cubes for numbers other than 1 to 10 using a list comprehension? Yes, by changing the range.
# 5. How would you modify the list comprehension to create a list of squares instead of cubes? Change value ** 3 to value ** 2.
# 6. What happens if you use a negative range in the list comprehension? It generates cubes for negative numbers.
# 7. Can you use a list comprehension to create a list of even cubes? Yes, by adding a condition in the comprehension.
# 8. How would you print each cube value on a separate line? Use a for
#    loop to iterate through the list and print each value.
