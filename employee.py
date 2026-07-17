#                    👨‍💼 Employee Management System

# -- Class Creation --
class Employee:
    def __init__(self, emp_id, name, age, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def displayDetails(self):
        print("\tEmployee ID : ", self.emp_id)
        print("\tName        : ", self.name)
        print("\tAge         : ", self.age)
        print("\tDepartment  : ", self.department)
        print(f"\tSalary      :  ₹{self.salary}\n")