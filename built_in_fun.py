t = (4, 1, 3, 2)

len(t)           # 4
min(t), max(t)   # 1, 4
sum(t)           # 10
sorted(t)        # [1, 2, 3, 4]  returns a LIST
tuple(sorted(t)) # (1, 2, 3, 4)
reversed(t)      # iterator
tuple(reversed(t))  # (2, 3, 1, 4)
any(t), all(t)   # True, True
enumerate(t)     # (index, value) pairs
zip(t, "abcd")   # pairs
3 in t           # True (membership, O(n))
3 not in t       # False
hash(t)          # works if all elements are hashable