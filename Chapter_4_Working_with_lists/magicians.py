magicians = ['alice', 'david', 'carolina']
for magician in magicians:  # Try to choose a meaningful name for the temporary variable
    print(magician)

'''It might help to read this code as
“For every magician in the list of magicians, print the magician’s name.”
The output is a simple printout of each name in the list:'''

# * alice
# * david
# * carolina
print()  # we added this to create a space (line break) between the two exercises

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

# *todo Check point page 53
