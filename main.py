class Menu:
    def __init__(self):
        self.dishes = {}

    def add_dish(self, name, price):
        self.dishes[name] = price

    def remove_dish(self, name):
        if name in self.dishes:
            del self.dishes[name]

    def get_price(self, name):
        return self.dishes.get(name)

class Order:
    def __init__(self):
        self.dishes = {}

    def add_dish(self, name, quantity):
        if name in self.dishes:
            self.dishes[name] += quantity
        else:
            self.dishes[name] = quantity

    def remove_dish(self, name, quantity):
        if name in self.dishes:
            if self.dishes[name] <= quantity:
                del self.dishes[name]
            else:
                self.dishes[name] -= quantity

    def calculate_total(self, menu):
        total = 0
        for dish, quantity in self.dishes.items():
            total += menu.get_price(dish) * quantity
        return total

class Table:
    def __init__(self, number):
        self.number = number
        self.order = Order()

    def add_dish(self, name, quantity, menu):
        self.order.add_dish(name, quantity)

    def remove_dish(self, name, quantity):
        self.order.remove_dish(name, quantity)

    def calculate_total(self, menu):
        return self.order.calculate_total(menu)

class Cashier:
    def __init__(self):
        self.tables = {}
        self.menu = Menu()

    def add_table(self, number):
        self.tables[number] = Table(number)

    def remove_table(self, number):
        if number in self.tables:
            del self.tables[number]

    def add_dish(self, table_number, name, quantity):
        if table_number in self.tables:
            self.tables[table_number].add_dish(name, quantity, self.menu)

    def remove_dish(self, table_number, name, quantity):
        if table_number in self.tables:
            self.tables[table_number].remove_dish(name, quantity)

    def calculate_total(self, table_number):
        if table_number in self.tables:
            return self.tables[table_number].calculate_total(self.menu)

    def print_menu(self):
        print("Menu:")
        for dish, price in self.menu.dishes.items():
            print(f"{dish}: {price}")

    def print_order(self, table_number):
        if table_number in self.tables:
            print(f"Order for table {table_number}:")
            for dish, quantity in self.tables[table_number].order.dishes.items():
                print(f"{dish}: {quantity}")

cashier = Cashier()
cashier.menu.add_dish("Pizza", 10)
cashier.menu.add_dish("Burger", 8)
cashier.add_table(1)
cashier.add_dish(1, "Pizza", 2)
cashier.add_dish(1, "Burger", 1)
print(cashier.calculate_total(1))
cashier.print_menu()
cashier.print_order(1)