def describe_city(city, country='UAE'):
    msg = city.title() + " is in " + country.title() + "."
    print(msg)
describe_city('Dubai')
describe_city('Kotayam', 'Kerala')
describe_city('Ajman')