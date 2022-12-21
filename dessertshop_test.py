"""importing dessert to create objects"""
import dessert as d

#key = Customer Name , value = Customer Object
customer_db = {}

# main creates instance of order class
def main_menu(order, customer_obj):
    """Asks for the users input"""
    try:
        menu = input(" 1:Candy \n 2:Cookie \n 3:Ice Cream \n 4:Sundae \n 5:Admin Module \n What would you like to add to the order? (1-5, Enter for done):" )
        if menu == "":
            print(order)
            customer_obj.add2history(order)
            print(f"Customer Name: {customer_obj.customer_name}\t\tCustomer ID: {customer_obj.customer_id}\t\tTotal Orders: {len(customer_obj.order_history[customer_obj.customer_name])}")
            new_order(order, customer_obj)
        elif menu == '1':
            user_prompt_candy(order, customer_obj)
        elif menu == '2':
            user_prompt_cookie(order, customer_obj)
        elif menu == '3':
            user_prompt_icecream(order, customer_obj)
        elif menu == '4':
            user_prompt_sundae(order, customer_obj)
        elif menu == '5':
            admin_menu_prompt(order, customer_obj)
    except ValueError:
            pass

def user_prompt_candy(order, customer_obj):
    """Creates a Candy in the Order"""
    candy_name = str(input("Enter the type of candy: "))
    candy_weight = float(input("Enter the weight: "))
    candy_price = float(input("Enter the price per pound: "))
    order.add(d.Candy(candy_name, candy_weight, candy_price))
    main_menu(order, customer_obj)

def user_prompt_cookie(order, customer_obj):
    """Creates a Cookie in the Order"""
    cookie_name = str(input("Enter the type of cookie: "))
    cookie_quantity = int(input("Enter the quantity: "))
    cookie_price = float(input("Enter the price per dozen: "))
    order.add(d.Cookie(cookie_name, cookie_quantity, cookie_price))
    main_menu(order, customer_obj)

def user_prompt_icecream(order, customer_obj):
    """Creates a IceCream in the Order"""
    icecream_name = str(input("Enter the type of ice cream: "))
    icecream_scoops = int(input("Enter the number of scoops: "))
    icecream_price = float(input("Enter the price per scoop: "))
    order.add(d.IceCream(icecream_name, icecream_scoops, icecream_price))
    main_menu(order, customer_obj)

def user_prompt_sundae(order, customer_obj):
    """Creates a Sundae in the Order"""
    icecream_name = str(input("Enter the type of ice cream: "))
    sundae_scoops = int(input("Enter the number of scoops: "))
    icecream_price = float(input("Enter the price per scoop: "))
    sundae_topping = str(input("Enter the topping: "))
    sundae_topping_price = float(input("Enter the price for the topping: "))
    order.add(d.Sundae(icecream_name, sundae_scoops, icecream_price, sundae_topping, sundae_topping_price))
    main_menu(order, customer_obj)

def new_order(order, customer_obj):
    """Asks customer if they would like to make a new order"""
    try:
        new_order_input = str(input("Start a new order. (y or n): "))
        if new_order_input == "y":
            order = d.Order()
            customer_obj = customer_prompt()
            payment_prompt(order)
            main_menu(order, customer_obj)
            new_order(order, customer_obj)
        elif new_order_input == "n":
            quit(print("\n Good Bye!"))
    except ValueError:
        pass

def admin_menu_prompt(order,customer_obj):
    """Admin Menu"""
    admin_menu = int(input("1: Shop Customer List\n2: Customer Order History\n3: Best Customer\n4: Exit Admin Module\nWhat would you like to do? (1-4):" ))
    if admin_menu == 1 or admin_menu == '1':
        for customer_obj, value in customer_db.items():
            print(f"Customer Name: {value.customer_name}\t\tCustomer ID:{value.customer_id}")
    elif admin_menu == 2:
        customer_search_name =input("Enter the name of the Customer:\n")
        if customer_search_name in customer_db:
            customer_obj = customer_db.get(customer_search_name)
            customer_order_history = customer_obj.order_history[customer_obj.customer_name]
            print(f"Customer Name: {customer_obj.customer_name}\t\tCustomer ID:{customer_obj.customer_id}")
            print("------------------------------------------------------------------------------------------")
            for i in range(len(customer_order_history)):
                order_obj_list = customer_order_history.get(i+1) #getting the items from history into a list
                order_obj = order_obj_list[0] #getting the order object for the payment type etc.
                for j , obj in enumerate(order_obj_list):
                    if j > 0:
                        order.add(obj)#setting the order list in the order obj
                print(f"Order #: {i+1}") #getting the order position, could change to the key at some point
                print(order_obj) #printing the order obj
                order.order.clear() #clearing the order list in the obj
    elif admin_menu == 3:
        names = []
        number_of_orders = []
        for i, obj in enumerate(customer_db):
                customer_obj = customer_db.get(obj)
                names.append(customer_obj.customer_name)
                number_of_orders.append(len(customer_obj.order_history[customer_obj.customer_name]))
        highest_orders = number_of_orders.index(max(number_of_orders))
        customer_obj = customer_db.get(names[highest_orders])
        print(f"The Dessert Shop's most valued customer is: {customer_obj.customer_name}!")
    elif admin_menu == 4:
        customer_obj = customer_prompt()
        payment_prompt(order)
        main_menu(order, customer_obj)

def customer_prompt():
    """Asks for customer info"""
    try:
        customer_name_input = str(input("Enter the customer name: "))
        if customer_name_input in customer_db:
            customer_obj = customer_db.get(customer_name_input)
            return customer_obj
        else:
            customer_db[(customer_name_input)] = d.Customer(customer_name_input, customer_id = 1000 + len(customer_db), next_customer_id = 1000 + (len(customer_db)+1))
            customer_obj = customer_db.get(customer_name_input)
            return customer_obj            
    except ValueError:
        pass

def payment_prompt(order):
    """Prompts the user for Payment Type"""
    try:
        payment_input = input(" 1:Cash \n 2:Card \n 3:Phone \n Enter Payment method: " )
        if payment_input == '1' or payment_input.lower() == "cash":
            order.pay_method = order.PayType.CASH
        elif payment_input == '2' or payment_input.lower() == "card":
            order.pay_method = order.PayType.CARD
        elif payment_input == '3' or payment_input.lower() == "phone":
            order.pay_method = order.PayType.PHONE
    except ValueError:
        pass

def main():
    """Is going to be used for the user interface"""
    order = d.Order()
    customer_obj = customer_prompt()
    payment_prompt(order)
    main_menu(order, customer_obj)

if __name__ == '__main__':
    main()
