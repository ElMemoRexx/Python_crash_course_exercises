
# todo 3-4 Guest List:
guests = ["Curry", "Jordan", "Cobby"]
for guest in guests:
    print(
        f"I would like to invite you to a nice dinner after the basketball match Mr. {guest}.")


# todo 3-5 Changing Guest List:
guests = ["Curry", "Jordan", "Cobby"]
print(f"\nUnfortunately, {guests[2]} can't make it to dinner.\n")
guests[2] = "Bryant"
for guest in guests:
    print(
        f"I would like to invite you to a nice dinner after the basketball match Mr. {guest}.")

# todo 3-6. More Guests:
guests = ["Curry", "Jordan", "Bryant"]
print(f"\nGood news everyone! We have found a bigger table.\n")
guests.insert(0, "Oneal")
guests.insert(2, "Green")
guests.append("Tatum")
for guest in guests:
    print(
        f"I would like to invite you to a nice dinner after the basketball match Mr. {guest}.")


# *todo 3-7. Shrinking Guest List:

# *You just found out that your new dinner table won’t
# *arrive in time for the dinner, and now you have space
# *for only two guests.
guests = ["Curry", "Jordan", "Bryant", "Oneal", "Green", "Tatum"]
for guest in guests:
    print(
        f"Unfortunately our dinner table wont's arrive on time for dinner, and now we only have space for two {guest}\n")
guests = guests[2:6]
for guest in guests:
    guests.pop()
    print(f"Sorry Mr. {guest}, we can't invite you to dinner.")

for guest in guests:
    print(f"\n Mr.{guest}, you are still invited to dinner.")

# Supón que tu lista final tiene dos invitados:
guests = ["Jordan", "Bryant"]

# Elimina el último invitado
del guests[-1]
# Elimina el que queda (ahora en la posición 0)
del guests[0]

# Imprime la lista para verificar que está vacía
print(guests)
