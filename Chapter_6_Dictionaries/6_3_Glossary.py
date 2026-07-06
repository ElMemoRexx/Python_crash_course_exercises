glossary = {
    'bool': 'A data type that can only be True or False.',
    'string': 'A sequence of characters enclosed in quotes.',
    'tuple': 'An ordered, immutable collection of elements.',
    'integer': 'A whole number without a decimal point.',
    'function': 'A reusable block of code that performs a specific task.'
}


# todo: continue from page 99, "looping Through All Key-Value Pairs"
for glossaries, meaning in glossary.items():
    print(f"\n{glossaries.title()}'s meaning is: ")
    print(f"{meaning}")
