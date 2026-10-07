# Problem: Determine triangle type from side lengths
# Equilateral: all sides equal
# Isosceles: two sides equal
# Scalene: all sides different
# Invalid: triangle inequality violated

a, b, c = 5, 5, 8

# Check validity first
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Invalid triangle")