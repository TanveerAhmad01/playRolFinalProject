import csv
import os
class Employee:
    def __init__(self, Employee_ID, name, PhoneNubr, role, Address):
        self.Employee_ID = Employee_ID
        self.name = name
        self.PhoneNubr = PhoneNubr
        self.role = role
        self.Address = Address

class AddEmployee(Employee):
    def __init__(self, Employee_ID, name, PhoneNubr, role, Address):
        super().__init__(Employee_ID, name, PhoneNubr, role, Address)




class AddDataIntoCsvFile:
    def __init__(self, employee):
        self.employee = employee

    def addData(self):
        file_exists = os.path.isfile('employees.csv')
        with open('employees.csv', 'a', newline='') as csvfile:
            fieldnames = ['Employee_ID', 'Name', 'PhoneNubr', 'Role', 'Address']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow({
                'Employee_ID': self.employee.Employee_ID,
                'Name': self.employee.name,
                'PhoneNubr': self.employee.PhoneNubr,
                'Role': self.employee.role,
                'Address': self.employee.Address
            })
            print("Employe added SuccessFully")


    def getDtaFromCsvFile(self):
        with open('employees.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(".............UserData...............") 
                for key, value in row.items():
                    print(f"{key}: {value}")




class DeleteEmployee(AddDataIntoCsvFile):
    def DeleteEmployee(self):
        userId = input("Enter userId to delete: ")

        with open('employees.csv', 'r', newline='') as csvfile, open('temp.csv', 'w', newline='') as tempcsv:
            fieldnames = ['Employee_ID', 'Name', 'PhoneNubr', 'Role', 'Address']
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            writer = csv.DictWriter(tempcsv, fieldnames=fieldnames)

            for row in reader:
                if row['Employee_ID'] != userId:
                    writer.writerow(row)

                    print("Employee Not Found")

                else:
                    print("Employee deleted successfully.")

       
        os.remove('employees.csv')
        os.rename('temp.csv', 'employees.csv')

                 
            

class updataUser(AddDataIntoCsvFile):
    def updataData(self):
        userId = input("Enter userId to Update: ")
        with open('employees.csv', 'r', newline='') as csvfile, open('temp.csv', 'w', newline='') as tempcsv:
            fieldnames = ['Employee_ID', 'Name', 'PhoneNubr', 'Role', 'Address']
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            writer = csv.DictWriter(tempcsv, fieldnames=fieldnames)
            for row in reader:
                if row['Employee_ID'] != userId:
                    writer.writerow(row)

                    print("Employee Not Found")

                else:
                    
                    print("Employee Updata successfully.")


