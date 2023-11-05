##Deli
sandwich_orders=['Vegetable','Cheese cooked','Chicken toast','Roast beef']
finished_sandwiches=[]
while sandwich_orders:
    this_sandwich=sandwich_orders.pop()
    print("I am working on your " + this_sandwich + "sandwich")
    finished_sandwiches.append(this_sandwich)
print("\n")
for sandwich in finished_sandwiches:
    print("I have made a" + sandwich + "sandwich")