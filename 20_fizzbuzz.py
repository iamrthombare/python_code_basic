# Problem: FizzBuzz - Classic conditional problem
# 1-100: Print "Fizz" for multiples of 3
# "Buzz" for multiples of 5
# "FizzBuzz" for multiples of both
# Number otherwise

for i in range(1, 101):
    if i % 15 == 0:  # Both 3 and 5
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)