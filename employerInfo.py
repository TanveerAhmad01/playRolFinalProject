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
    def DeleteEmploye(self):
        userId = input("Enter userId to delete: ")
        print(type(userId))
        rows_to_keep = []

        with open('employees.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                employee_id = row[0]
                

                if employee_id != userId:
                    rows_to_keep.append(row)

        with open('employees.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows_to_keep)
            print("Employee with userId", userId, "deleted successfully.")
                        
                    
class updataUser(AddDataIntoCsvFile):
     def updateData(self):
        userId = input("Enter userId to update: ")
        print(type(userId))
        updated_data = []

      
        with open('employees.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                employee_id = row[0]
                if employee_id == userId:
                   
                    new_name = input("Enter new name: ")
                    new_phone = input("Enter new phone number: ")
                    new_role = input("Enter new role: ")
                    new_address = input("Enter new address: ")
                    row = [employee_id, new_name, new_phone, new_role, new_address]
                updated_data.append(row)

       
        with open('employees.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(updated_data)

        print("Employee with userId", userId, "updated successfully.")


