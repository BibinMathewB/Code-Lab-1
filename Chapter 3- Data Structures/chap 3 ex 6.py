"""You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.

•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

•Print a message to each of the two people still on your list, letting them know they’re still invited."""

# Invite some people to dinner.
guests=['Mark Twine', 'Jack turner', 'Jhonson']
name=guests[0].title()
print(name + ", I would like to invite you to our dinner, do humbly request you to accept.")

name=guests[1].title()
print(name + ",I would like to invite you to our dinner, do humbly request you to accept.")

name=guests[2].title()
print(name + ",I would like to invite you to our dinner, do humbly request you to accept.")

name=guests[1].title()
print("\nSorry, " + name + "won't be able to make it to the dinner.")
# Jack can't make it! Let's invite Gary instead.
del(guests[1])
guests.insert(1,'gary snyder')

# Print the invitations again.
name=guests[0].title()
print("\n" + name + ", I would like to invite you to our dinner, do humbly request you to accept.")

name=guests[1].title()
print(name + ", I would like to invite you to our dinner, do humbly request you to accept.")

name=guests[2].title()
print(name + ", I would like to invite you to our dinner, do humbly request you to accept.")
# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'frida kahlo')
guests.insert(2, 'reinhold messner')
guests.append('elizabeth peratrovich')

name=guests[0].title()
print(name + ",I would like to invite you to our dinner, do humbly request you to accept.")

name=guests[1].title()
print(name + ",I would like to invite you to our dinner, do humbly request you to accept.")

name=guests[2].title()
print(name + ",I would like to invite you to our dinner, do humbly request you to accept.")

name=guests[3].title()
print(name + ",I would like to invite you to our dinner, do humbly request you to accept.")

name=guests[4].title()
print(name + ",I would like to invite you to our dinner, do humbly request you to accept.")

name=guests[5].title()
print(name + ",I would like to invite you to our dinner, do humbly request you to accept.")
# Oh no, the table won't arrive on time!
print("\nSorry,we can only invite two people to dinner.")

name=guests.pop()
print("Sorry," + name.title() + "there's no room at the table.")

name=guests.pop()
print("Sorry," + name.title() + "there's no room at the table.")

name=guests.pop()
print("Sorry," + name.title() + "there's no room at the table.")

name=guests.pop()
print("Sorry," + name.title() + "there's no room at the table.")
# There should be two people left. Let's invite them.
name = guests[0].title()
print(name + ",I would like to invite you to our dinner, do humbly request you to accept.")

name=guests[1].title()
print(name + ",I would like to invite you to our dinner, do humbly request you to accept.")
# Empty out the list.
del(guests[0])
del(guests[0])
# Prove the list is empty.
print(guests)