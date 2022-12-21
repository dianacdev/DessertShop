"""Used to make a class abstract or a method"""
from abc import ABC, abstractmethod
import functools
from packaging import Packaging
from payment import Payment


@functools.total_ordering
class DessertItem(ABC):
    """Superclass Dessert Item used to create other Items"""

    def __init__(self, name: str, tax_percent=7.25, cost = 0.00):
        self.name = name
        self.tax_percent = tax_percent
        self.cost = cost

    @abstractmethod
    def calculate_cost(self):
        """Calculates the cost"""

    def calculate_tax(self):
        """Calculates the tax"""
        tax = self.cost * (self.tax_percent / 100)
        return tax

    @property
    def packaging(self):
        """Getting the package type"""
        return self._packaging

    @packaging.setter
    def packaging(self, package_type):
        self._packaging = package_type


    def is_valid_operand(self, other):
        """Checking that it is a valid operand"""
        return hasattr(other, "cost")

    def __eq__(self, other):
        if not self.is_valid_operand(other):
            return NotImplemented
        return self.cost == other.cost

    def __lt__(self, other):
        return self.cost > other.cost

class Candy(DessertItem, Packaging):
    """Candy class used to instantiate a candy Object"""
    def __init__(self, name: str,  candy_weight=1.0,  price_per_pound=1.00):
        DessertItem.__init__(self, name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
        self.packaging = "Bag"

    def is_same_as(self, other: "Candy") -> bool:
        """Using Type Hinting to ensure that if two objects are of the same type it returns True"""
        if self.name == other.name:
            if self.price_per_pound == other.price_per_pound:
                return True
        else:
            return False

    def calculate_cost(self):
        """Calculates the cost of Candy"""
        self.cost = self.candy_weight * self.price_per_pound
        return self.cost

    def __str__(self):
        return f"{self.name} ({self.packaging})\n{self.candy_weight:>8}lbs @ ${self.price_per_pound}/lb:\t\t${self.calculate_cost():.2f}\t[Tax: ${self.calculate_tax():.2f}]"

class Cookie(DessertItem, Packaging):
    """Cookie class used to instantiate a cookie Object"""

    def __init__(self, name: str,  cookie_quantity=12, price_per_dozen=5.00):
        DessertItem.__init__(self, name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
        self.packaging = "Box"

    def is_same_as(self, other: "Cookie") -> bool:
        """Using Type Hinting to ensure that if two objects are of the same type it returns True"""
        if self.name == other.name:
            if self.price_per_dozen == other.price_per_dozen:
                return True
        else:
            return False

    def calculate_cost(self):
        """Calculates the cost of Cookie"""
        self.cost = (self.cookie_quantity/12) * self.price_per_dozen
        return self.cost

    def __str__(self):
        return f"{self.name} Cookies ({self.packaging})\n{self.cookie_quantity:>5} @ ${self.price_per_dozen:.2f}/dozen:\t\t${self.calculate_cost():.2f}\t[Tax: ${self.calculate_tax():.2f}]"

class IceCream(DessertItem,Packaging):
    """IceCream class used to instantiate a ice cream Object"""

    def __init__(self, name: str,  scoop_count=1, price_per_scoop=1.50):
        DessertItem.__init__(self, name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.packaging = "Bowl"

    def calculate_cost(self):
        """Calculates the cost of IceCream"""
        self.cost = self.scoop_count * self.price_per_scoop
        return self.cost

    def __str__(self):
        return f"{self.name} Ice Cream ({self.packaging})\n{self.scoop_count:>5} scoops @ ${self.price_per_scoop:.2f}/scoop\t${self.calculate_cost():.2f}\t[Tax: ${self.calculate_tax():.2f}]"

class Sundae(IceCream, DessertItem,Packaging):
    """Sundae class used to instantiate a sundae Object"""

    def __init__(self,name:str,scoop_count=2,price_per_scoop=0.5,topping_name="",topping_price=0.5):
        DessertItem.__init__(self, name)
        IceCream.__init__(self, name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
        self.name = (topping_name+ " " +name + " Sundae")
        self.packaging = "Boat"

    def calculate_cost(self):
        """Calculates the cost or Sundae"""
        self.cost = (self.scoop_count * self.price_per_scoop) + self.topping_price
        return self.cost

    def __str__(self):
        return f"{self.name} ({self.packaging})\n{self.scoop_count:>5} scoops @ ${self.price_per_scoop:.2f}/scoop\n{self.topping_name:>13} topping @ ${self.topping_price:.2f}:\t${self.calculate_cost():.2f}\t[Tax: ${self.calculate_tax():.2f}]"

class Order(Payment):
    """Creating an Order"""
    order = []
    PayType = Payment.PayType
    pay_method = PayType.CASH

    @property
    def pay_type(self):
        """Getting the paytype"""
        return self.pay_type

    @pay_type.setter
    def pay_type(self, pay_method):
        self.pay_type = pay_method

    def add(self, item):
        """Adds a Dessert Item to the Order"""
        if item.__class__ == Candy:
            for i, obj in enumerate(self.order):
                if Candy.is_same_as(item, obj):
                    item.candy_weight = item.candy_weight + obj.candy_weight
                    self.order.pop(i)
        elif item.__class__ == Cookie:
            for i, obj in enumerate(self.order):
                if Cookie.is_same_as(item, obj):
                    item.cookie_quantity = item.cookie_quantity + obj.cookie_quantity
                    self.order.pop(i)
        self.order.append(item)

    def item_count(self):
        """Gives the number of items in the Order"""
        return len(self.order)

    def order_cost(self):
        """Gives the total cost for all items in the order"""
        subtotal = 0
        for obj in self.order:
            subtotal += obj.calculate_cost()
        return subtotal

    def order_tax(self):
        """Gives the total tax for all items in the order"""
        total_tax = 0
        for obj in self.order:
            total_tax += obj.calculate_tax()
        return total_tax


    def __str__(self):
        print("\n \t ---------------Receipt---------------")

        for i, obj in enumerate(self.order): #Bubble sort
            for j in range(0, len(self.order)-i-1):
                if self.order[j].calculate_cost() > self.order[j+1].calculate_cost():
                    self.order[j], self.order[j+1] = self.order[j+1], self.order[j]
        for obj in self.order:
            print(obj.__str__())
        print("------------------------------------------------------")
        print(f'Total number of items in order: {self.item_count()}')
        print(f'Order Subtotals:|         ${self.order_cost():.2f}                  [Tax: ${self.order_tax():,.2f}]')
        print(f'Order Total:                                      ${(self.order_cost()+self.order_tax()):,.2f}')
        print("------------------------------------------------------")
        print(f'Paid with {self.pay_method.name}')
        print("------------------------------------------------------")
        return ""

class Customer(Order):
    """Creates a Customer"""
    order = Order() #might not need this
    order_history = {}

    def __init__(self, customer_name:str, customer_id:int, next_customer_id:int):
        self.customer_name = customer_name
        self.next_customer_id = next_customer_id
        self.customer_id = customer_id

    def add2history(self, order:order):
        """Adds to the Customers History"""
        if self.customer_name in self.order_history: #repeating code can create a function to call for this if
            order_id = len(self.order_history[self.customer_name])
            self.order_history[self.customer_name][order_id+1] = []
            self.order_history[self.customer_name][order_id+1].append(order)
            for obj in order.order:
                self.order_history[self.customer_name][order_id+1].append(obj)
            Order.order.clear()
        else:
            self.order_history[self.customer_name] = {}
            order_id = len(self.order_history[self.customer_name])
            self.order_history[self.customer_name][order_id+1] = []
            self.order_history[self.customer_name][order_id+1].append(order)
            for obj in order.order:
                self.order_history[self.customer_name][order_id+1].append(obj)
            Order.order.clear()
