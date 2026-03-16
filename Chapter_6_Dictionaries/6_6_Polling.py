
# * 6-6. Polling: Use the code in favorite_languages.py (page 96).
"""
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.
"""
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people_to_poll = ['jen', 'phil', 'ana', 'carlos', 'sarah', 'mario']

for name in people_to_poll:
    if name in favorite_languages:
        language = favorite_languages[name].title()
        print(
            f"\nThank you {name.title()} for taking the poll! We know you love {language}")

    else:
        print(
            f"\nHi {name.title()}, we'd love to know your favorite programming language! Please take our poll.")
