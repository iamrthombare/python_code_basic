# Problem: Demonstrate short-circuit evaluation
# Second condition not evaluated if first determines result

def check_positive(x):
    print(f"Checking {x}")
    return x > 0

# and: stops at first False
print("--- and (short-circuits at False) ---")
result = check_positive(5) and check_positive(-3) and check_positive(10)
print(f"Result: {result}")

print("\n--- or (short-circuits at True) ---")
result = check_positive(-5) or check_positive(3) or check_positive(10)
print(f"Result: {result}")