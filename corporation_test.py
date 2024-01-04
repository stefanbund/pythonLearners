# Import random module
import random

# Define some lists of adjectives and products
adjectives = ["fancy", "spicy", "crunchy", "soft", "sweet", "sour", "bitter", "salty", "fresh", "frozen"]
products = ["cake", "pizza", "burger", "salad", "sandwich", "soup", "ice cream", "coffee", "tea", "soda"]

# Define a class for product
class Product:
    # Initialize a product with a random name and a random price
    def __init__(self):
        self.name = random.choice(adjectives) + " " + random.choice(adjectives) + " " + random.choice(adjectives) + " " + random.choice(products)
        self.price = round(random.uniform(1, 10), 2)

    # Return the name and price of the product
    def __str__(self):
        return self.name + " ($" + str(self.price) + ")"

# Define a class for inventory
class Inventory:
    # Initialize an inventory with a list of products
    def __init__(self):
        self.products = []
        # Generate a random number of products between 10 and 20
        num_products = random.randint(10, 20)
        # Add products to the inventory
        for i in range(num_products):
            self.products.append(Product())

    # Return the list of products in the inventory
    def __str__(self):
        result = "Inventory:\n"
        for product in self.products:
            result += str(product) + "\n"
        return result

# Define a class for store
class Store:
    # Initialize a store with a name, an inventory, a list of customers, and a sale object
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
        self.customers = []
        self.sale = Sale()

    # Add a customer to the store
    def add_customer(self, customer):
        self.customers.append(customer)

    # Run the simulation for the store
    def run(self):
        print("Welcome to " + self.name + "!")
        print(self.inventory)
        print("We have " + str(len(self.customers)) + " customers today.")
        # Iterate over the customers
        for customer in self.customers:
            print("Customer " + customer.name + " is shopping.")
            # Take one item from the inventory and add it to the customer's basket
            item = random.choice(self.inventory.products)
            customer.add_to_basket(item)
            print("Customer " + customer.name + " added " + str(item) + " to their basket.")
            # Increment the sale object with the price of the item
            self.sale.increment(item.price)
            print("Customer " + customer.name + " checked out and paid $" + str(item.price) + ".")
        print("The total sales for " + self.name + " today is $" + str(self.sale.total) + ".")

    # Return the name and the sale object of the store
    def __str__(self):
        return self.name + " (Sales: $" + str(self.sale.total) + ")"

# Define a class for customer
class Customer:
    # Initialize a customer with a name and a basket
    def __init__(self, name):
        self.name = name
        self.basket = Basket()

    # Add a product to the customer's basket
    def add_to_basket(self, product):
        self.basket.add(product)

    # Return the name and the basket of the customer
    def __str__(self):
        return self.name + " (" + str(self.basket) + ")"

# Define a class for basket
class Basket:
    # Initialize a basket with a list of products
    def __init__(self):
        self.products = []

    # Add a product to the basket
    def add(self, product):
        self.products.append(product)

    # Return the list of products in the basket
    def __str__(self):
        result = "Basket:\n"
        for product in self.products:
            result += str(product) + "\n"
        return result

# Define a class for sale
class Sale:
    # Initialize a sale with a total amount
    def __init__(self):
        self.total = 0

    # Increment the total amount by a given price
    def increment(self, price):
        self.total += price

    # Return the total amount of the sale
    def __str__(self):
        return "Sale: $" + str(self.total)

# Define a class for corporation
class Corporation:
    # Initialize a corporation with a name and a list of stores
    def __init__(self, name):
        self.name = name
        self.stores = []

    # Add a store to the corporation
    def add_store(self, store):
        self.stores.append(store)

    # Run the simulation for the corporation
    def run(self):
        print("Welcome to " + self.name + "!")
        print("We have " + str(len(self.stores)) + " stores in our corporation.")
        # Iterate over the stores
        for store in self.stores:
            # Run the simulation for each store
            store.run()
        # Calculate the total sales for the corporation
        total_sales = 0
        for store in self.stores:
            total_sales += store.sale.total
        print("The total sales for " + self.name + " today is $" + str(total_sales) + ".")

    # Return the name and the list of stores of the corporation
    def __str__(self):
        result = self.name + ":\n"
        for store in self.stores:
            result += str(store) + "\n"
        return result

# Create a corporation object
corp = Corporation("Bing Corp")

# Create some store objects and add them to the corporation
store1 = Store("Bing Store 1")
store2 = Store("Bing Store 2")
store3 = Store("Bing Store 3")
corp.add_store(store1)
corp.add_store(store2)
corp.add_store(store3)

# Create some customer objects and add them to the stores
customer1 = Customer("Alice")
customer2 = Customer("Bob")
customer3 = Customer("Charlie")
customer4 = Customer("David")
customer5 = Customer("Eve")
customer6 = Customer("Frank")
customer7 = Customer("Grace")
customer8 = Customer("Harry")
customer9 = Customer("Ivy")
customer10 = Customer("Jack")
store1.add_customer(customer1)
store1.add_customer(customer2)
store2.add_customer(customer3)
store2.add_customer(customer4)
store2.add_customer(customer5)
store3.add_customer(customer6)
store3.add_customer(customer7)
store3.add_customer(customer8)
store3.add_customer(customer9)
store3.add_customer(customer10)

# Run the simulation for the corporation
corp.run()
