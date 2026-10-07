set1 = {10, 20, 30}
set2 = {1, 2, 3}

list1 = sorted(list(set1))     # list construcot is used for converting set into list  after that sorting it  
list2 = sorted(list(set2))

for i in range(len(list1)):
    print(list1[i] + list2[i])