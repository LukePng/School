class Grocery:
    def __init__(self, title, cost, price, stock):
        self._title = title
        self._cost = cost
        self._price = price
        self._stock = stock
    
    def set_title(self, new_title):
        self._title = new_title

    def set_cost(self, new_cost):
        self._cost = new_cost
    
    def set_price(self, new_price):
        self._price = new_price

    def get_title(self):
        return self._title
    
    def get_cost(self):
        return self._cost
    
    def get_price(self):
        return self._price
    
    def get_stock(self):
        return self._stock
    
    def update_stock(self, change_in_stock):
        self._stock += change_in_stock
    
    def calculate_final_price(self):
        return self._price
    
    def __str__(self):
        return "{:<20} |  {:>6.2f} |  {:>6.2f} | {:>6} |  {:>12.2f}".format(self._title, self._cost, self._price, self._stock, self.calculate_final_price())
    
class ElectricalAppliance(Grocery):
    def __init__(self, title, cost, price, stock, power):
        super().__init__(title, cost, price, stock)
        self._power = power

    def get_power(self):
        return self._power
    
    def calculate_final_price(self):
        if self._power <= 10:
            return super().calculate_final_price() * 0.8 * 1.07
        return super().calculate_final_price() * 1.07

class Cigarette(Grocery):
    def __init__(self, title, cost, price, stock, nicotine_content):
        super().__init__(title, cost, price, stock)
        self._nicotine_content = nicotine_content

    def get_nicotine_content(self):
        return self._nicotine_content
    
    def calculate_final_price(self):
        return super().calculate_final_price() * 1.6 * 1.07
    
class Alcohol(Grocery):
    def __init__(self, title, cost, price, stock, type):
        super().__init__(title, cost, price, stock)
        self._type = type

    def get_type(self):
        return self._type
    
    def calculate_final_price(self):
        if self._type == 'wine':
            return super().calculate_final_price() * 1.5 * 1.07
        elif self._type == 'beer':
            return super().calculate_final_price() * 1.2 * 1.07
        else:
            return super().calculate_final_price() * 1.07
        
class StoreManager:
    def __init__(self, grocery_list):
        self._grocery_list = grocery_list

    def sell_item(self, sold_item):
        for i in self._grocery_list:
            if i.get_title() == sold_item[0]:
                i.update_stock(-sold_item[1])
                print("{:<20} |  {:>6} |  {:>6} | {:>6}".format(
                "Title", "Price", "Quantity sold", "Subtotal"))
                print("{:-^65}".format(""))
                print("{:<20} |  {:>6.2f} |  {:>6} | {:>6.2f}".format(i.get_title(), i.get_price(), sold_item[1], i.get_price()*sold_item[1]))
                break
    def sell_items(self, sold_items):
        print("{:<20} |  {:>6} |  {:>6} | {:>6}".format("Title", "Price", "Quantity sold", "Subtotal"))
        print("{:-^65}".format(""))
        for item in sold_items:
            for i in self._grocery_list:
                if i.get_title() == item[0]:
                    i.update_stock(-item[1])
                    
                    print("{:<20} |  {:>6.2f} |  {:>6} | {:>6.2f}".format(i.get_title(), i.get_price(), item[1], i.get_price()*item[1]))
                    break

    def stock_check(self):
        print("{:<20} |  {:>6} | {:>12}".format("Title", "Unit Cost", "Quantity Left"))
        print("{:-^40}".format(""))
        for i in self._grocery_list:
            if i.get_stock()<5:
                print("{:<20} | ${:>6.2f} | {:>12}".format(i.get_title(), i.get_cost(), i.get_stock()))



    

####################################################
# Please do not modify the code below
####################################################


def initialise_data():
    g1 = Grocery("Spoon", 1.5, 2.5, 15)
    g2 = Grocery("Fork", 1.7, 3.0, 5)
    g3 = Grocery("Shampoo", 5.2, 11, 11)
    g4 = Grocery("Power Cable", 6.5, 15, 12)

    ea1 = ElectricalAppliance("Normal Light Bulb 01", 2, 3, 3, 25)
    ea2 = ElectricalAppliance("Normal Light Bulb 02", 2.5, 4, 6, 30)
    ea3 = ElectricalAppliance("LED Light Bulb", 6, 10, 9, 5)
    ea4 = ElectricalAppliance("Desk Light", 30, 50, 2, 50)
    ea5 = ElectricalAppliance("LED Desk Light", 40, 60, 15, 10)

    c1 = Cigarette("Marlboro Red", 27.65, 35, 15, 0.7)
    c2 = Cigarette("Bomond Blue", 12.10, 15, 12, 0.7)
    c3 = Cigarette("Camel Filters", 23.38, 30, 23, 0.6)
    c4 = Cigarette("Yun Yan", 16.5, 23, 4, 0.65)

    a1 = Alcohol("Barefoot", 55, 86, 3, "wine")
    a2 = Alcohol("Great Wall", 45, 80, 5, "wine")
    a3 = Alcohol("Hardys", 57, 90, 6, "wine")
    a4 = Alcohol("Coors Light", 15, 27, 13, "beer")
    a5 = Alcohol("Tsingtao", 10, 20, 7, "beer")

    return [g1, g2, g3, g4, ea1, ea2, ea3, ea4, ea5, c1, c2, c3, c4, a1, a2, a3, a4, a5]


g_list = initialise_data()


def test_function_5_1():
    print("Begin test function 5.1\n")

    print("{:-^65}".format("Current Grocery List"))
    print("{:<20} |  {:>6} |  {:>6} | {:>6} |  {:>12}".format(
        "Title", "Cost", "Price", "Stock", "Final Price"))
    print("{:-^65}".format(""))

    for g in g_list:
        print(g)

    print("\nEnd of test function 5.1\n")


test_function_5_1()


def test_function_5_2():
    print("Begin test function 5.2\n")
    sm = StoreManager(g_list)
    sold_item_list = [("Spoon", 2), ("Fork", 3)]
    sm.sell_items(sold_item_list)

    print()
    sm.stock_check()

    print("\nEnd of test function 5.2\n")

test_function_5_2()