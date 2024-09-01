# inventory.py

class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        # Initialize the Shoe object with provided attributes
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        # Return the cost of the shoe
        return self.cost

    def get_quantity(self):
        # Return the quantity of the shoe
        return self.quantity

    def __str__(self):
        # Return a string representation of the Shoe object
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"

# List to store Shoe objects
shoe_list = []

def read_shoes_data():
    # Read data from inventory.txt and create Shoe objects
    try:
        with open('inventory.txt', 'r') as file:
            next(file)  # Skip the header line
            for line in file:
                # Parse the line to extract shoe details
                country, code, product, cost, quantity = line.strip().split(',')
                shoe = Shoe(country, code, product, float(cost), int(quantity))
                shoe_list.append(shoe)
    except FileNotFoundError:
        print("The file inventory.txt does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def capture_shoes():
    # Capture shoe details from user input and create a new Shoe object
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    cost = float(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    # Append the new shoe data to the inventory file
    with open('inventory.txt', 'a') as file:
        file.write(f"\n{country},{code},{product},{cost},{quantity}")

def view_all():
    # Print details of all Shoe objects in the shoe_list
    for shoe in shoe_list:
        print(shoe)

def re_stock():
    # Find the Shoe object with the lowest quantity and restock it
    if not shoe_list:
        print("No shoes available.")
        return
    min_quantity_shoe = min(shoe_list, key=lambda s: s.get_quantity())
    print(f"Shoe to restock: {min_quantity_shoe}")
    add_quantity = int(input("Enter quantity to add: "))
    min_quantity_shoe.quantity += add_quantity
    update_inventory_file()

def search_shoe():
    # Search for a Shoe object by its code and print its details
    code = input("Enter shoe code: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            return
    print("Shoe not found.")

def value_per_item():
    # Calculate and print the total value of each Shoe object
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"Product: {shoe.product}, Value: {value}")

def highest_qty():
    # Find the Shoe object with the highest quantity and print its details
    if not shoe_list:
        print("No shoes available.")
        return
    max_quantity_shoe = max(shoe_list, key=lambda s: s.get_quantity())
    print(f"Shoe with highest quantity: {max_quantity_shoe}")

def update_inventory_file():
    # Update the inventory.txt file with the current list of Shoe objects
    with open('inventory.txt', 'w') as file:
        file.write("country,code,product,cost,quantity\n")
        for shoe in shoe_list:
            file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

def main():
    read_shoes_data()
    while True:
        # Display menu options to the user
        print("\nMenu:")
        print("1. Capture Shoes")
        print("2. View All Shoes")
        print("3. Re-stock Shoes")
        print("4. Search Shoe")
        print("5. Calculate Value Per Item")
        print("6. Find Shoe with Highest Quantity")
        print("0. Exit")
        choice = input("Enter your choice: ")
        
        # Execute the corresponding function based on user's choice
        if choice == '1':
            capture_shoes()
        elif choice == '2':
            view_all()
        elif choice == '3':
            re_stock()
        elif choice == '4':
            search_shoe()
        elif choice == '5':
            value_per_item()
        elif choice == '6':
            highest_qty()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
