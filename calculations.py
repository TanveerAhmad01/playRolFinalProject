import csv
from datetime import datetime

class SalaryCalculator:
    def __init__(self):
        self.employee_data = []

    def load_employee_data(self):
        with open('employees.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.employee_data.append(row)

    def record_salary(self):
        print("Record salary for each employee:")
        for employee_info in self.employee_data:
            salary = float(input(f"Enter salary for employee {employee_info['Employee_ID']}: "))
            employee_info['Salary'] = salary

    def record_hours_worked(self):
        date_today = datetime.now().strftime("%Y-%m-%d")
        time_now = datetime.now().strftime("%H:%M:%S")
        print("Record hours worked for today:", date_today)
        for employee_info in self.employee_data:
            hours_worked = input(f"Enter hours worked for employee {employee_info['Employee_ID']} today: ")
            employee_info['Hours_Worked'] = hours_worked

    def calculate_monthly_salary(self):
        for employee_info in self.employee_data:
            hourly_rate = employee_info.get('Salary', 0) / (30 * 8)  # Assuming 30 days and 8 hours per day
            employee_info['Hourly_Rate'] = hourly_rate

    def save_employee_data(self):
        with open('employees.csv', 'w', newline='') as csvfile:
            if not self.employee_data:
                print("No employee data to save.")
                return
            fieldnames = list(self.employee_data[0].keys())  # Get all keys from the first employee data entry
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for employee_info in self.employee_data:
                writer.writerow(employee_info)

    def get_total_monthly_income(self):
        total_income = sum(employee.get('Salary', 0) for employee in self.employee_data)
        return total_income
