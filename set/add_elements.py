a = set();
print(type(a));
#add()   this fiunction is used for the adding elements
a.add(1);
a.add(2);
print(a);

# update(iterable) this function is used for the multiple value is can add in the set
                    # tuple set list

b = set();
b.update([1,2,4,5,6]);  # list
b.update((8,94,949)); # tuple
b.update((8,9,99));

for i in b:
    print(i);   # set cannot add duplicate value 


