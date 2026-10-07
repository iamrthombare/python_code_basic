from scipy.constants import elementary_charge

f = ["apple", "banana", "cherry"]

# append   add the element at last
f.append("orange")
print(f)

# extend add the group of element and its allow the tuple for extending yhe list
f.extend((1,2,3,))
f.extend((4,5,6,))
f.extend((1,1,1,1,1))
print(f)

# insert (index,element)  add the specific index
f.insert(100,"chiku")
f.insert(-2,100) # skip the 2 index from last and then add
print(f)

# remove (element)   check from staring then remove only 1 elemnt if find
f.remove(3)
print(f)

if 1 in f:
    f.remove(1)
print(f)

# pop(index)  remove the specific index and return it
f.pop(6)
print(f.pop()) #  remove the last element
print(f.pop(-1))

a = [10, 20, 30, 20, 40]

print(a.index(20))        # 1   (first match)
print(a.index(20, 2))     # 3   (search from index 2)
print(a.index(20, 2, 4))  # 3   (search in index 2 to 3)

# a.index(99)             # ValueError: 99 is not in list

# clear()  used remove everythinhg in the list
a.clear()
# count(element)   this methood is used for the counting the element in list
f.count(1)

# index(x, start, end): find the position of a value

a = [10, 20, 30, 20, 40]

print(a.index(20))        # 1   (first match)
print(a.index(20, 2))     # 3   (search from index 2)
print(a.index(20, 2, 4))  # 3   (search in index 2 to 3)


# sort method sorting the list by deafult asceding
a = [3, 1, 4, 2]
a.sort()
print(a)             # [1, 2, 3, 4]

a.sort(reverse=True)    # for the  desceding order sort(reverse=True)
print(a)             # [4, 3, 2, 1]