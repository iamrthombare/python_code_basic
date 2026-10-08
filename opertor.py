(1, 2) + (3,)        # (1, 2, 3)   concatenation, creates new tuple
(1, 2) * 3           # (1, 2, 1, 2, 1, 2)
(1, 2) == (1, 2)     # True
(1, 2) < (1, 3)      # True: lexicographic comparison
(1, 2, 3) < (1, 3)   # True (2 < 3 decides)
(1, 2) < (1, 2, 0)   # True (shorter prefix is smaller)