
# * 6-7. People:
""" Start with the program you wrote for Exercise 6-1 (page 98). Make
two new dictionaries representing different people, and store all three
dictio-naries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person"""
people = [
    {
        'fname': 'guillermo',
        'lname': 'hernandez',
        'age': 32,
        'city': 'cancun',
    },
    {
        'fname': 'mario',
        'lname': 'ramirez',
        'age': 38,
        'city': 'cdmx',
    },
    {
        'fname': 'alana',
        'lname': 'hernandez',
        'age': 1,
        'city': 'cdmx',
    }
]

for person in people:
    full_name = (f"{person['fname']} {person['lname']}")
    age = person['age']
    location = person['city']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    print(f"\tage: {age}")
