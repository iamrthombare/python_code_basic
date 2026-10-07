# Calculate the Average of Set Elements
# Write a Python program to create a set of integers and calculate the average of all elements.
from fontTools.merge.util import avg_int

a = {1,2,3,4,4,5}

print(avg_int(a))
print(sum(a)/len(a))    # /  division opertor consider the points value


sum = 0
for i in a:
    sum+=i
print(sum//len(a))  # // floor division remove the point value 