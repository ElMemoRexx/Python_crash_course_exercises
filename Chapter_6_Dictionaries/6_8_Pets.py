
# * 6-8. Pets:
# Make several dictionaries, where each dictionary represents a different pet.
# In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list
# and as you do, print everything you know about each pet.
pets = [
    {
        'name': 'cooper',
        'color': 'pink',
        'type': 'amphibian',
        'owner': 'matt',
    },

    {
        'name': 'mathilda',
        'color': 'black',
        'type': 'feline',
        'owner': 'guillermo',
    },

    {
        'name': 'mike',
        'color': 'blue',
        'type': 'canine',
        'owner': 'willie',
    }
]

for pet in pets:
    pet_name = pet['name']
    pet_color = pet['color']
    pet_type = pet['type']
    pet_owner = pet['owner']

    print(f"\tName: {pet_name.title()}")
    print(f"\tColor: {pet_color.title()}")
    print(f"\tType: {pet_type.title()}")
    print(f"\tOwner: {pet_owner.title()}")
