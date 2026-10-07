# Problem: Check if a year is a leap year
# Divisible by 4, but not by 100 unless also divisible by 400

year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Test cases
test_years = [2000, 1900, 2020, 2021, 2024]
for y in test_years:
    is_leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
    print(f"{y}: {'Leap' if is_leap else 'Not leap'}")