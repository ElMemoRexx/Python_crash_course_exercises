my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # * we make a copy of the list

# print("My favorite foods are:")  # *we print a message
my_foods.append('cannoli')  # * we add a new food to the original list

# print("\nMy friend's favorite foods are:")
friend_foods.append('ice cream')  # * we add a new food to the copied list

print("My favorite foods are:")
print(my_foods)  # * we print both lists to show they are different

print("\nMy friend's favorite foods are:")
print(friend_foods)  # * we print the copied list
