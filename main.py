from employerInfo import *

userInput = input("""
Press:
1: Add Employees
2: Delete Data
3: Update Data
4:View Empolye              
""")

if userInput == '1':
    Employee_ID = input("Employee_ID::")
    name = input("name::")
    PhoneNubr = input("PhoneNubr::")
    role = input("role::")
    Address = input("Address::")

    new_employee = AddEmployee(Employee_ID, name, PhoneNubr, role, Address)
    add_data = AddDataIntoCsvFile(new_employee)
    add_data.addData()
elif userInput == "2":
    ViewData = DeleteEmployee(employee="")
    ViewData.DeleteEmployee()
    

elif userInput == "3":
        pass


elif userInput == "4":
    ViewData = AddDataIntoCsvFile(employee="")
    ViewData.getDtaFromCsvFile()