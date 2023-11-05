##No Pastrami

sandwich_orders=['Pastrami','Vegetables','Cheese cooked','Chicken toast','Roast beef']
finished_sandwiches=[]
print("I'm sorry, Pastrami is out of stock.")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')
print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I am working on your" + current_sandwich + "sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\n")
for sandwich in finished_sandwiches:
    print("I have made a" + sandwich + "sandwich.")