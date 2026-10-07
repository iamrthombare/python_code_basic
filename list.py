a = ["abc", "fed",1,"hhh","ttt",2,3]
print(a)
a.pop(3)  #index
print(a)
print(a[-1]) # start from reverse

# slicing operator on list
# lsit[start:end:step]    start always with its equal index and end with less than 1
print(a[1:3])  # start correct from and end with less than 1
print(a[:3])   # from 0 indexing to start and end less than 1
print(a[2:])  # exatacking starting from index and goes end
print(a[::-1]) # reverse the list by 1 by 1 step
print(a[::-2]) # skip 2 elemets form ending and then print
print(a[:])  # print staring from ending full list
print(a[-4:])  # when we use - then start from ending use negative indixing last
print(a[:-2]) # when we use - sign then skip last elenemt
print(a[-3:-1])

