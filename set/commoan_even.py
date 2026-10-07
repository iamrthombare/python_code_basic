# 10.Find Common Even Numbers
#
# Write a Python program to create two sets and display the common elements that are even numbers.
# Sample Input:


a = {1, 2, 5, 4, 6, 12}
b = {2, 3, 4, 5, 12, 35}

for x in a | b:
    if x % 2 == 0:
        print(x)