emp ={}

size = int(input("Enter the size of employee:"))

for i in range(size):
    id = int(input("Enter employee name:"))
    salary = int(input("Enter salary:"))
    emp[id] = salary

for id, salary in emp.items():
    print("Employee id:",id)
    print("Salary:",salary)
