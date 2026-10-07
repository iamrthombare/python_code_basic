import sys

a = {1,2,3,4,5,5}
print(max(a))

max =   - (sys.maxsize -1)
for x in a:
    if x > max:
        max = x
print("max element: " ,max)

#Find the Minimum Element
#Write a Python program to create a set of integers and find the smallest element in the set.
print(min(a))

import sys

min_val = sys.maxsize

for x in a:
    if x < min_val:
        min_val = x

print("min element:", min_val)
