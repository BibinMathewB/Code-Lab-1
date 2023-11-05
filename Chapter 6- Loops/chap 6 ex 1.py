Pizza="\nWhat topping would you like on your pizza?"
Pizza+="\nType 'quit' when you are finished:"

while True:
    topping=input(Pizza)
    if topping != 'quit':
        print("I'll add " + topping + " to your pizza")
    else:
        break