# Problem: Check if a number is positive, negative, or zero
# Then check if positive number is even or odd

number = 4

if number > 0:
    print("Positive")
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
elif number < 0:
    print("Negative")
else:
    print("Zero")