def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
print(fact(5))


def table(x, y):
    if y <= 10:
        print(x * y)
        table(x, y + 1)

table(20, 1)