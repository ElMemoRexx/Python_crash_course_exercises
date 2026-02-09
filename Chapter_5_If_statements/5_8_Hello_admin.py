
# * 5-8 Hello Admin:
'''Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user.'''

users = ['admin', 'Paul', 'Guillermo', 'Saul', 'Alana']
for user in users:
    if user == 'admin':
        print(f'¡Hello {user}, would you like to see a status report?')
    else:
        print(f'¡Hello {user}, thank your for logging in again.')


# todo: Continue from excercise 5-9
