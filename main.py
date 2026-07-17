#                     👨‍💼 Employee Management System

# -- Importing class from employee.py --
from employee import Employee

# -- Importing functions from helpers.py --
from helpers import getEmployeeId, getEmployeeName, getEmployeeAge, getEmployeeDepartment, getEmployeeSalary, saveEmployees, loadEmployees

# -- Each object added into List --
employees = loadEmployees()

# -- Navigation Menu-driven Creation ---
while True:
    print("===================================")
    print("     EMPLOYEE MANAGEMENT SYSTEM    ")
    print("===================================")
    print("\t1. Add Employee")
    print("\t2. View All Employees")
    print("\t3. Search Employee")
    print("\t4. Update Employee")
    print("\t5. Delete Employee")
    print("\t6. Employee Count")
    print("\t7. Highest Paid Employee")
    print("\t8. Lowest Paid Employee")
    print("\t9. Average Salary")
    print("\t10. Exit")
    print()

    try:
        option =  int(input("Enter your option (1-10): "))

        # -- 1. Add Employee Option --
        if option == 1:
            print("\n======= Add Employee =======")
            employee_id = getEmployeeId()
            employee_name = getEmployeeName()
            employee_age = getEmployeeAge()
            employee_department = getEmployeeDepartment()
            employee_salary = getEmployeeSalary()

            # -- Object Creation --
            newEmployee = Employee(employee_id, employee_name, employee_age, employee_department, employee_salary)

            # -- Duplicate Employee ID prevention --
            if not employees:
                employees.append(newEmployee)  # current object added into 'employees' list
                saveEmployees(employees)       # 'employees' list passed into function definition
                print("\nEmployee added successfully.\n")
            else:
                for emp in employees:
                    if employee_id == emp.emp_id:
                        print(f"\nEmployee already exists with ID '{employee_id}'👎\n")
                        break
                else:
                    employees.append(newEmployee)  # current object added into 'employees' list
                    saveEmployees(employees)       # 'employees' list passed into function definition
                    print("\nEmployee added successfully.\n")

        # -- 2. View All Employees Option --
        elif option == 2:
            print("\n======= View All Employee =======")
            if not employees:
                print("No employees available.\n")
            else:
                print(f"\nTotal Employees: {len(employees)}")
                count = 0
                for emp in employees:
                    count += 1
                    print(f"{count}.")
                    emp.displayDetails()

        # -- 3. Search Employee Option --
        elif option == 3:
            print("\n======= Search Employee =======")
            if not employees:
                print("No employees available.\n")
            else:
                employee_id = getEmployeeId()
                print()
                print("======== Employee Details ========")
                for emp in employees:
                    if emp.emp_id == employee_id:
                        emp.displayDetails()
                        break
                else:
                    print("Employee not found.\n")

        # -- 4. Update Employee Option --
        elif option == 4:
            print("\n======= Update Employee =======")
            if not employees:
                print("No employees available.\n")
            else:
                employee_id = getEmployeeId()

                for emp in employees:
                    if emp.emp_id == employee_id:

                        # -- Function Call for Updating Employee details by ID --
                        employee_name = getEmployeeName()
                        employee_age = getEmployeeAge()
                        employee_department = getEmployeeDepartment()
                        employee_salary = getEmployeeSalary()

                        # -- Updating Instance Variables Value --
                        emp.name = employee_name
                        emp.age = employee_age
                        emp.department = employee_department
                        emp.salary = employee_salary
                        saveEmployees(employees)
                        print("\nEmployee updated successfully.\n")
                        break
                else:
                    print("Employee not found.\n")

        # -- 5. Delete Employee Option --
        elif option == 5:
            print("\n======= Delete Employee =======")
            if not employees:
                print("No employees available.\n")
            else:
                employee_id = getEmployeeId()

                for emp in employees:
                    if emp.emp_id == employee_id:
                        employees.remove(emp)
                        saveEmployees(employees)
                        print("\nEmployee deleted successfully.\n")
                        break
                else:
                    print("Employee not found.\n")

        # -- 6. Employee Count Option --
        elif option == 6:
            print("\n======= Employee Count =======")
            if not employees:
                print("No employees available.")
            else:
                print(f"Total Employees: {len(employees)}\n")

        # -- 7. Highest Paid Employee Option --
        elif option == 7:
            print("\n======= Highest Paid Employee =======")
            if not employees:
                print("No Employees available.\n")
            else:
                highest_salary = 0
                for emp in employees:
                    if emp.salary > highest_salary:
                        highest_salary = emp.salary

                count = 0
                for emp in employees:
                    if emp.salary == highest_salary:
                        count += 1
                        print(f"{count}.")
                        emp.displayDetails()

        # -- 8. Lowest Paid Employee Option --
        elif option == 8:
            print("\n======= Lowest Paid Employee =======")
            if not employees:
                print("No Employees available.\n")
            else:
                lowest_salary = employees[0].salary
                for emp in employees:
                    if emp.salary < lowest_salary:
                        lowest_salary = emp.salary

                count = 0
                for emp in employees:
                    if emp.salary == lowest_salary:
                        count += 1
                        print(f"{count}.")
                        emp.displayDetails()

        # -- 9. Average Salary Option --
        elif option == 9:
            print("\n======= Average Salary =======")
            if not employees:
                print("No Employees available.\n")
            else:
                total_salary = 0
                for emp in employees:
                    total_salary += emp.salary

                average_salary = total_salary // len(employees)
                print(f"Average Salary : ₹{average_salary}\n")

        # -- 10. Exit Option --
        elif option == 10:
            print("Thank you!")
            break

        else:
            print("Invalid Option, Choose between 1-10\n")

    except ValueError:
        print("Invalid input!\n")