favorite_number = {
    'mark': 14,
    'daniel': 2,
    'oscar': 78,
    'emmanuel': 32,
    'willie': 3
}

print(favorite_number['mark'])

for name, number in favorite_number.items():
    print(f"\n{name.title()}'s favorite numbers are: ")
    print(f"\t{number}")
