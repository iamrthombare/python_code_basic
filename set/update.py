from IPython.terminal.shortcuts.auto_suggest import \
    discard  # there will be not update method bcoz its have no indexing but we can do it using if  and add remove and discard

a= set()
a.add(1)
a.update(set(range(1,10)))
print(a)

if 2 in a:
    a.discard(2);  # we can use remove method 
    a.add(10);
print(a)
