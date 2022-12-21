''' payroll.py main function Illustrates the payroll module. '''
from payroll import *
import os, os.path, shutil

employees = []
PAY_LOGFILE = "payroll.txt"


def main():
    """Loads the employees, processes the timecards, processes receipts and runs the payroll"""
    def run_payroll():
        # pay_log_file is a global variable holding ‘payroll.txt’
        if os.path.exists(PAY_LOGFILE):
            os.remove(PAY_LOGFILE)
        for emp in employees:  # employees is the global list of Employee objects
            emp.issue_payment()  # issue_payment calls a method in the classification
        # object to compute the pay
    def load_employees():
        """Loads all the employees and classifies them"""
        with open('employees.csv', 'r', encoding='utf-8') as file_obj:
            file_obj = file_obj.readlines()[1:]
            for row in file_obj:  # classification: 3=Hourly, 2=Commissioned, 1=Salary
                row = row.split(',')
                if row[7] == '3':
                    employee = Employee(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    employee.make_hourly(row[10])
                elif row[7] == '2':
                    employee = Employee(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    employee.make_commissioned(row[8],row[9])
                elif row[7] == '1':
                    employee = Employee(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    employee.make_salaried(row[8])
                employees.append(employee)

    def process_timecards():
        """Adds the hours worked for Hourly employees"""
        with open('timecards.csv', 'r', encoding='utf-8') as file_obj:
            file_obj = file_obj.readlines()
            hourly_employees = []
            for emp in employees:
                if  emp.__class__ == Hourly:
                    emp.hours_worked = 0
                    hourly_employees.append(emp)
            for row in file_obj:
                row = row.split(',')
                for emp in hourly_employees:
                    if row[0] == emp.emp_id:
                        hours_worked = 0
                        hours_list = row[1:]
                        hours_list = list(map(float, hours_list))
                        for i, hours in enumerate(hours_list):
                            hours_worked += hours
                        emp.hours_worked = hours_worked

    def process_receipts():
        """Processes the sales made by Commissioned Employees"""
        with open('receipts.csv', 'r', encoding='utf-8') as file_obj:
            file_obj = file_obj.readlines()
            commissioned_employees = []
            for emp in employees:
                if emp.__class__ == Commissioned:
                    emp.total_sales = 0
                    commissioned_employees.append(emp)
            for row in file_obj:
                row = row.split(',')
                for emp in commissioned_employees:
                    if row[0] == emp.emp_id:
                        total_sales = 0
                        sales_list = row[1:]
                        sales_list = list(map(float, sales_list))
                        for i, sales in enumerate(sales_list):
                            total_sales += sales
                        emp.total_sales = total_sales

    def find_employee_by_id(emp_id):
        """Finding the employee using its emp_id"""
        for emp in employees:
            if emp.emp_id == emp_id:
                return emp

    load_employees()
    process_timecards()
    process_receipts()
    run_payroll()

    # Save copy of payroll file; delete old file
    shutil.copyfile(PAY_LOGFILE, 'paylog_old.txt')
    if os.path.exists(PAY_LOGFILE):
        # You define PAY_LOGFILE = ‘paylog.txt’ globally
        os.remove(PAY_LOGFILE)

    # Change Issie Scholard to Salaried by changing the Employee object:
    emp = find_employee_by_id('51-4678119')
    emp.make_salaried(134386.51)
    emp.issue_payment()

    # Change Reynard,Lorenzin to Commissioned; add some receipts
    emp = find_employee_by_id('11-0469486')
    emp.make_commissioned(50005.50, 27)
    clas = emp
    clas.add_receipt(1109.73)
    clas.add_receipt(746.10)
    emp.issue_payment()

    # Change Jed Netti to Hourly; add some hour entries
    emp = find_employee_by_id('68-9609244')
    emp.make_hourly(47)
    clas = emp
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    emp.issue_payment()
2,083.5625




if __name__ == '__main__':
    main()
