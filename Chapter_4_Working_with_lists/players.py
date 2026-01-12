players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # we get the first three players in the list
print(players[1:4])  # we get the second, third, and fourth players in the list
print(players[:4])   # we get the first four players in the list
print(players[2:])   # we get all players from the third player to the end
print(players[-3:])  # we get the third player from the end of the list

print("\nHere are the first three players on my team:")  # * we print a message
for player in players[:3]:  # * we loop through the first three players in the list
    # * we print each player's name with the first letter capitalized
    print(player.title())
