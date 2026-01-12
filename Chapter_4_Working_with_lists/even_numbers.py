even_numbers = list(range(2, 11, 2))  # * List of even numbers from 2 to 10
print(even_numbers)

squares = []
for value in range(1, 11):  # * List of squares of numbers from 1 to 10
    # square = value ** 2 # * Calculate the square of the value, but this is not necessary and makes the code longer
    # * Append the square of the value to the list , this is also a more concise way to do it
    squares.append(value ** 2)
print(squares)
