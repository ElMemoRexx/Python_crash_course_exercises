
# * 6-10. Favorite Numbers:
'''
Modify your program from Exercise 6-2 (page 98) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.
'''

favorite_number = {
    'mark': [14, 20],
    'daniel': [2, 3],
    'oscar': [78, 6],
    'emmanuel': [32, 4, 7],
    'willie': [3, 1]
}


for name, numbers in favorite_number.items():
    print(f"\n{name.title()}'s favorite numbers are: ")
    for number in numbers:
        print(f"\t{number}")

# todo: Continue from excercise 6-11 from page 111
