# Problem: Check truthy/falsy values
# Empty strings, 0, None, empty lists are falsy

value = ""

if value:
    print("Truthy")
else:
    print("Falsy")

# More examples
print(bool(0))        # False
print(bool(1))        # True
print(bool("hello"))  # True
print(bool(""))       # False
print(bool([]))       # False
print(bool([1]))      # True
print(bool(None))     # False