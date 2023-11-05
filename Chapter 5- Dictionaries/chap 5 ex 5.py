"""Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about 

each pet"""

#An empty list to store the pets in
animals=[]

#Make individual pets, and store each one in the list
pet1={
    'animal type': 'Crocodile',
    'name': 'Flash',
    'owner': 'Aamir',
    'weight': 43,
    'eats': 'Bugs'}
animals.append(pet1)

pet2={
    'animal type': 'chicken',
    'name': 'Pood',
    'owner': 'Abdul',
    'weight': 2,
    'eats': 'Seeds',}
animals.append(pet2)

pet3={
    'animal type': 'dog',
    'name': 'Patrick',
    'owner': 'Godvin',
    'weight': 37,
    'eats': 'Shoes',}
animals.append(pet3)

#Display information about each pet
for pet in animals:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value)) 
