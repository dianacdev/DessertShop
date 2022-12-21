"""Used to make a class abstract or a method"""
from abc import ABC
import csv

class Employee(ABC):
    """Superclass for Employees, similar to DessertItem"""
    def __init__(self, emp_id, first_name, last_name, address, city, state, zipcode) -> None:
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def issue_payment(self):
        """Used to issue payment to the Employee by printing to payroll.txt"""
        return self

    def make_hourly(self, hourly_rate):
        """Make hourly Employee"""
        self.__class__ = Hourly
        self.hourly_rate = hourly_rate
        self.classification = '3'

    def make_commissioned(self, salary_rate, commission_rate):
        """Make hourly Employee"""
        self.__class__ = Commissioned
        self.salary_rate = salary_rate
        self.commission_rate = commission_rate
        self.classification = '2'

    def make_salaried(self, salary_rate):
        """Make hourly Employee"""
        self.__class__ = Salary
        self.salary_rate = salary_rate
        self.classification = '1'

class Classification(ABC):  # abstract class for the 3 types of classification
    """Class for the 3 types of classification"""
    def compute_pay(self):
        """Used to compute the pay for each Employee, should be overwritten depending on classification"""
        return self

class Hourly(Employee, Classification):
    """An Employee that is Hourly"""
    def __init__(self, emp_id: str, first_name: str, last_name: str, address: str, city: str, state: str, zipcode: str, classification=3, hourly_rate=1.00, hours_worked = 0.0) -> None:
        Employee.__init__(self, emp_id, first_name, last_name,
                          address, city, state, zipcode)
        self.classification = classification
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def compute_pay(self):
        """Used to pay Salary"""
        pay_per_period = self.hours_worked * float(self.hourly_rate)  # bi-weekly pay
        pay_per_period = round(pay_per_period,2)
        return pay_per_period

    def issue_payment(self): #Adds entry to payroll.txt file
        """Prints an entry into the payroll.txt file"""
        #self.compute_pay()
        with open('payroll.txt','a', encoding='utf-8') as f:
            f.write(f"Mailing {self.compute_pay()} to {self.first_name} {self.last_name} at {self.address} {self.city} {self.state} {self.zipcode}\n")
        return "Added entry to payroll.txt"

    def add_timecard(self, hours):
        """Adds hours worked to user and logs hours worked in timecards.csv"""
        hours_list = []
        with open('timecards.csv','a', encoding='utf-8') as f:
            f.write(self.emp_id)
        with open('timecards.csv','r', encoding="utf-8") as file:
            file = file.readlines()
            hours_worked = 0
            hours_list.append(hours)
            for i, sale in enumerate(hours_list):
                hours_worked += sale
            self.hours_worked = hours_worked
        with open('timecards.csv','a', encoding='utf-8') as f:
            f.write(","+str(hours)+"\n")

class Salary(Employee, Classification):
    """An Employee that is Salary"""
    def __init__(self, emp_id: str, first_name: str, last_name: str, address: str, city: str, state: str, zipcode: str, classification= 1, salary_rate=1.00) -> None:
        Employee.__init__(self, emp_id, first_name, last_name,
                          address, city, state, zipcode)
        self.classification = classification
        self.salary_rate = salary_rate

    def compute_pay(self):
        """Used to pay Salary"""
        pay_per_period = float(self.salary_rate)/24
        pay_per_period = round(pay_per_period,2)
        return pay_per_period

    def issue_payment(self): #Adds entry to payroll.txt file
        """Prints an entry into the payroll.txt file"""
        #self.compute_pay()
        with open('payroll.txt','a', encoding='utf-8') as f:
            f.write(f"Mailing {self.compute_pay()} to {self.first_name} {self.last_name} at {self.address} {self.city} {self.state} {self.zipcode}\n")
        return "Added entry to payroll.txt"

class Commissioned(Salary, Classification):
    """An Employee that is Commissioned"""
    def __init__(self, emp_id: str, first_name: str, last_name: str, address: str, city: str, state: str, zipcode: str, commission_rate=1.00, total_sales = 0) -> None:
        Salary.__init__(self, emp_id, first_name, last_name,
                        address, city, state, zipcode, salary_rate=1.00)
        self.classification = 2
        self.commission_rate = commission_rate
        self.total_sales = total_sales

    def compute_pay(self):
        """Used to pay Salary"""
        pay_per_period = (float(self.salary_rate)/24) + ((float(self.commission_rate)/100) * float(self.total_sales))
        pay_per_period = round(pay_per_period,2)
        return pay_per_period

    def issue_payment(self): #Adds entry to payroll.txt file
        """Prints an entry into the payroll.txt file"""
        #self.compute_pay()
        with open('payroll.txt','a', encoding='utf-8') as f:
            f.write(f"Mailing {self.compute_pay()} to {self.first_name} {self.last_name} at {self.address} {self.city} {self.state} {self.zipcode}\n")
        return "Added entry to payroll.txt"

    def add_receipt(self, sale):
        """Adds hours worked to user and logs hours worked in timecards.csv"""
        receipts = []
        with open('receipts.csv','a', encoding='utf-8') as f:
            f.write(self.emp_id)
        with open('receipts.csv','r', encoding="utf-8") as file:
            file = file.readlines()
            total_sales = 0
            receipts.append(sale)
            for i, sale in enumerate(receipts):
                total_sales += sale
            self.total_sales = total_sales
        with open('receipts.csv','a', encoding='utf-8') as f:
            f.write(","+str(sale)+"\n")
                


