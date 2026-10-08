student = {
    "name": "John",
    "age": 20
}

try:
    print(student["grade"])

except KeyError:
    print("Key not found in dictionary.")