
# * 6-4. Glossary 2:
'''Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When
you’re sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output.'''

glossary = {
    'bool': 'A data type that can only be True or False.',
    'string': 'A sequence of characters enclosed in quotes.',
    'tuple': 'An ordered, immutable collection of elements.',
    'integer': 'A whole number without a decimal point.',
    'function': 'A reusable block of code that performs a specific task.',
    'list': 'An ordered, mutable collection of elements enclosed in square brackets.',
    'dictionary': 'A collection of key-value pairs enclosed in curly braces.',
    'loop': 'A control structure that repeats a block of code multiple times.',
    'conditional': 'A statement that executes code based on whether a condition is true or false.',
    'variable': 'A named container that stores a value in memory.'
}

for key, value in glossary.items():
    print(f"\n{key.title()}, {value}")
