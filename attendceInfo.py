import csv
from datetime import datetime

class Attendance:
    def __init__(self):
        self.attendance_data = {}

    def take_attendance(self):
        date_today = datetime.now().strftime("%Y-%m-%d")
        time_now = datetime.now().strftime("%H:%M:%S")

        print("Take attendance for today:", date_today)

        attendance_list = []
        with open('employees.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                employee_id = row[0] 
                attendance = input(f"Is employee {employee_id} present? (Y/N): ")
                attendance_list.append((employee_id, attendance, date_today, time_now))

        self.attendance_data[date_today] = attendance_list

    def save_attendance_to_csv(self):
        with open('employees.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

        header_row = rows[0]
        if "Attendance" not in header_row:
            header_row.extend(["Attendance", "Date", "Time"])
            rows[0] = header_row

        for date_today, attendance_list in self.attendance_data.items():
            for employee_id, attendance, date, time in attendance_list:
                for row in rows[1:]:
                    if row[0] == employee_id:
                        row.extend([attendance, date, time]) 
                        break

        with open('employees.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)


