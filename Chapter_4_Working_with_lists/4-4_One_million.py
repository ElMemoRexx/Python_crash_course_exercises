# *4-4. One Million:
'''Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing CTRL-C or by closing the output window.)'''
million = list(range(1, 1000001))
for value in million:
    print(value)

# Alternative solution using a for loop and append():
million = []
for value in range(1, 1000001):
    million.append(value)
for value in million:
    print(value)
# Note: The list of a million numbers is not printed to avoid performance issues.
print(million)
# million = --- IGNORE ---
