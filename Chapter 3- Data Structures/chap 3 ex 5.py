"""You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.

•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still in your list."""

# Invite some people to dinner
guests=['Mark Twine', 'Jack turner', 'Jhonson']
name=guests[0].title()
print(name + ",I would like to invite you to our dinner, do humbly request you to accept.")

name=guests[1].title()
print(name + ",I would like to invite you to our dinner, do humbly request you to accept.")

name=guests[2].title()
print(name + ",I would like to invite you to our dinner, do humbly request you to accept.")

name=guests[0].title()
print("\nSorry, " + name + " can't make it to dinner.")
# Mark can't make it so Let's invite Indo instead.
del(guests[0])
guests.insert(0, 'Indo swine')
# Print the invitations again
name=guests[0].title()
print("\n" + name + ",I would like to invite you to our dinner, do humbly request you to accept.")

name=guests[1].title()
print(name + ",I would like to invite you to our dinner, do humbly request you to accept.")

name=guests[2].title()
print(name + ",I would like to invite you to our dinner, do humbly request you to accept.")