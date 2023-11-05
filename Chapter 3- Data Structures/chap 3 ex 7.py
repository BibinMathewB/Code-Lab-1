Location=['Dubai', 'Texas', 'Thailand', 'Hamburg', 'Georgia']

print("Original order:")
print(Location)

print("\nAlphabetical:")
print(sorted(Location))

print("\nOriginal order:")
print(Location)

print("\nReverse alphabetical:")
print(sorted(Location, reverse=True))

print("\nOriginal order:")
print(Location)

print("\nReversed:")
Location.reverse()
print(Location)

print("\nOriginal order:")
Location.reverse()
print(Location)

print("\nAlphabetical")
Location.sort()
print(Location)

print("\nReverse alphabetical")
Location.sort(reverse=True)
print(Location)