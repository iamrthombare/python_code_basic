a = set();

a.add(1);
a.add(1);
a.add(1);
a.add(2);
a.add(3);
a.update({4,5,6});
print(a);

# remove() remive the specific element in the set
a.remove(1);
print(a)

a.discard(7);  # if prsent then reomve otherwise it not show thw error
print(a)

a.pop()   # remove elements randomly
a.pop()
print(a)


a.clear();  # clear the set
print(a)