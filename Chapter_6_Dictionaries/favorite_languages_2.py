favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}


if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"\nHi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
