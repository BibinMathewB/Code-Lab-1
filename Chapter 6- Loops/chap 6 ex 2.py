Subject="How old are you guys/Mr./Mdm.?"
Subject+="\nType 'quit' when you are finished:"
while True:
    age=input(Subject)
    if age=='quit':
        break

    age=int(age)
    if age < 3:
        print("You get in for free since you are a child")
    elif age < 13:
        print("Your ticket is for $10")
    else:
        print("Your ticket is for $15")