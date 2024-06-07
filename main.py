from employerInfo import *
from calculations import *
from attendceInfo import *

class Main:

    def addEmployee():
        Employee_ID = input("Employee ID: ")
        name = input("Name: ")
        PhoneNubr = input("Phone Number: ")
        role = input("Role: ")
        Address = input("Address: ")

        new_employee = AddEmployee(Employee_ID, name, PhoneNubr, role, Address)
        add_data = AddDataIntoCsvFile(new_employee)
        add_data.addData()


    def markAttendance():
        attendance = Attendance()
        attendance.take_attendance()
        attendance.save_attendance_to_csv()

    def calculateSalary():
        calculator = SalaryCalculator()
        calculator.load_employee_data()
        calculator.record_salary()  # Record salary first
        calculator.record_hours_worked()  # Then record hours worked
        calculator.calculate_monthly_salary()
        calculator.save_employee_data()
        calculator.get_total_monthly_income()

 
    def menu():
        while True:
            userInput = input("""
    Press:
    1: Add Employees
    2: Mark Attendance
    3: Salary
    4: Exit
    """)

            if userInput == '1':
                Main.addEmployee()
            elif userInput == '2':
                Main.markAttendance()
            elif userInput == '3':
                Main.calculateSalary()
            elif userInput == '4':
                break
            else:
                print("Invalid input. Please try again.")

if __name__ == "__main__":
    Main.menu()
