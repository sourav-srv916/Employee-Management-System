#                     👨‍💼 Employee Management System

# -- Importing class from employee.py --
from employee import Employee

# -- Employee ID Getting and Validation --
def getEmployeeId():
    while True:
        try:
            getting_employee_id = int(input("Enter Employee ID: "))
            break
        except ValueError:
            print("Invalid input! ID must be a number.")
    return getting_employee_id

# -- Employee Name Getting and Validation --
def getEmployeeName():
    while True:
        getting_employee_name = input("Enter Name: ")
        if getting_employee_name.replace(" ", "").isalpha():
            break
        else:
            print("Invalid input! Employee name must contain only letters.")
    return getting_employee_name

# -- Employee Age Getting and Validation --
def getEmployeeAge():
    while True:
        try:
            getting_employee_age = int(input("Enter Age: "))
            if 18 <= getting_employee_age <= 60:
                break
            else:
                print("Age must be between 18 and 60")
        except ValueError:
            print("Invalid input! Age must be a number.")
    return getting_employee_age

# -- Employee Department Getting and Validation --
def getEmployeeDepartment():
    while True:
        getting_employee_department = input("Enter Department Name: ")
        if getting_employee_department.replace(" ", "").isalpha():
            break
        else:
            print("Invalid input! Department name must contain only letters.")
    return getting_employee_department

# -- Employee Salary Getting and Validation --
def getEmployeeSalary():
    while True:
        try:
            getting_employee_salary = float(input("Enter Salary: "))
            if getting_employee_salary > 0:
                break
            else:
                print("Salary must be greater than 0.")
        except ValueError:
            print("Invalid input! Salary must be a number.")
    return getting_employee_salary

# -- Entire Employee data saved into Text file --
def saveEmployees(employees_list):
    with open("employees.txt", "w") as employee_file:
        for employee in employees_list:
            data = f"{employee.emp_id},{employee.name},{employee.age},{employee.department},{employee.salary}\n"
            employee_file.write(data)

# Load Employee data from Text file before program start --
def loadEmployees():
    load_employees = []
    try:
        with open("employees.txt", "r") as employee_file:
            for line in employee_file:
                line = line.strip()
                data = line.split(",")
                loadEmployee = Employee(int(data[0]),data[1],int(data[2]),data[3],float(data[4]))
                load_employees.append(loadEmployee)
    except FileNotFoundError:
        pass
    return load_employees