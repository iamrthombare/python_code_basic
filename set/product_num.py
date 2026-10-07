#9.Find the Product of All Elements
#Write a Python program to create a set of integers and calculate the product of all elements.

a = {1,2,3,4,5,6,7,8,9}
mul = 1

for i in a:
    mul *= i
print(mul)
