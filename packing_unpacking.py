# Packing
t = 1, 2, 3

# Unpacking
a, b, c = t

# Swap without a temp variable
a, b = b, a

# Star unpacking
first, *middle, last = (1, 2, 3, 4, 5)
# first=1, middle=[2, 3, 4], last=5   (middle is always a LIST)

head, *tail = (1, 2, 3)      # head=1, tail=[2, 3]
*init, last = (1, 2, 3)      # init=[1, 2], last=3

# Ignore values
a, _, c = (1, 2, 3)

# Nested unpacking
(a, (b, c)), d = (1, (2, 3)), 4

# Unpacking in function calls
def f(x, y, z): ...
f(*(1, 2, 3))

# Merging
t = (*(1, 2), *(3, 4), 5)    # (1, 2, 3, 4, 5)

# Mismatch error
a, b = (1, 2, 3)   # ValueError: too many values to unpack