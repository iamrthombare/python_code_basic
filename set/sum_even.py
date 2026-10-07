#Find the Sum of Even Numbers
#Write a Python program to create a set of integers and calculate the sum of only the even numbers.


a = set(range(1,20))
print(a)

sum = 0
for i in a:
    if i % 2 == 0:
        sum += i
print("sum of even num :",sum)


