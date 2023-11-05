"""Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

* Use a loop to print the name of each river included in the dictionary.

* Use a loop to print the name of each country included in the dictionary."""

Rivers={
    'Nile': 'Egypt',
    'Sao Francisco': 'Brazil',
    'Huang He': 'West China',
    'Kuskokwim': 'Alaska',
    'Mississippi': 'United States',}
for river, country in Rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

print("\nFollowing rivers are included in this set:")
for river in Rivers.keys():
    print("- " + river.title())

print("\nFollowing countries are included in this set:")
for country in Rivers.values():
    print("- " + country.title())