# Problem: Simple login system with multiple conditions
# Check username, password, and account status

username = "admin"
password = "secret123"
is_active = True
attempts = 3

# Simulated database
correct_username = "admin"
correct_password = "secret123"

if not is_active:
    print("Account is disabled")
elif attempts <= 0:
    print("Too many failed attempts. Account locked.")
elif username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Invalid username or password")