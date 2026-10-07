 # Operation	Method	Operator	Result

 # Union	A.union(B)	A | B
a = {1,2,3,4,5,6,7,8,9,1}
b = {1,2,3,4,5,11,23,44,55,77,88}
print(a|b)  # all value print comman and uncommand
print(a.union(b))

 # Intersection	A.intersection(B)	A & B
print(a&b)  # all value print comman and uncommand
print(a.intersection(b))

 # Difference	A.difference(B)	A - B
print(a.difference(b))   # set a and set b command element remove only set a uncommand element return
print(a-b)


 # Symmetric Difference	A.symmetric_difference(B)	A ^ B
print(a.symmetric_difference(b))  # only uncommnan element show
print(a^b)