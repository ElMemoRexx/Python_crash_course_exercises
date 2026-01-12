
# * 4-11. My Pizzas, Your Pizzas:
'''Start with your program from Exercise 4-1 (page 56).
Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the
following:'''

# *1. Add a new pizza to the original list.
# *2. Add a different pizza to the list friend_pizzas.
# *3. Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My
# * friend’s favorite pizzas are:, and then use a for loop to print the second list.
# * Make sure each new pizza is stored in the appropriate list.

pizzas_list = ["Peperoni", "Hawaiian", "Mexican", "Veggie", "BBQ Chicken"]
friend_pizzas = pizzas_list[:]
pizzas_list.append("Buffalo Chicken")
friend_pizzas.append("Four Cheese")

print("My favorite pizzas are:")  # * we print a message
for pizza in pizzas_list:  # * we loop through the first three pizzas in the list
    # * we print each pizza's name with the first letter capitalized
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")  # * we print a message
for pizza in friend_pizzas:  # * we loop through the first three pizzas in the list
    # * we print each pizza's name with the first letter capitalized
    print(f"- {pizza}")
