a=set([1,2,3,4,5])
b= set((2,4,5))

print(a.issubset(b));  # a all value presnt in the b if prsent then true othewise false
print(a.issuperset(b));     # b all value prsent is in a
print(a.isdisjoint(b)); # no comman element in a and b if comman then false