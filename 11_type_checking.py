# Problem: Perform different actions based on data type
# Using isinstance()

value = 42

if isinstance(value, int):
    print("Integer")
elif isinstance(value, float):
    print("Float")
elif isinstance(value, str):
    print("String")
elif isinstance(value, list):
    print("List")
else:
    print("Other type")