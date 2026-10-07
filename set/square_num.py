#Find the Square of Each Element
#Write a Python program to create a set of integers and create a new set containing the square of each element

a = set(range(1,11))
print(a)
#square = set()
for i in a.copy():  # at the iteration tym we cannot remove and add  error Set changed size during iteration
    a.add(i*i);
    a.remove(i)

print(a)
