# Using f-strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

# Make it a title
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")


# This code displays the message Hello, Ada Lovelace! as well, but by
# assigning the message to a variable 1 we make the final print() call much
# simpler 2.
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"  # 1
print(message)  # 2
