# Product dictionary
products = {}

def add_product(products):
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    products[name] = price
    print(f"Added {name} with price {price}")

def update_price(products):
    name = input("Enter product name to update: ")
    if name in products:
        price = float(input("Enter new price: "))
        products[name] = price
        print(f"Updated {name} to price {price}")
    else:
        print("Product not found.")

def find_in_range(products):
    low = float(input("Enter lower price: "))
    high = float(input("Enter upper price: "))
    found = [name for name, price in products.items() if low <= price <= high]
    print(f"Products in price range {low} to {high}: {found}")

while True:
    print("\nMenu:")
    print("1. Add new product")
    print("2. Update price of existing product")
    print("3. Find products within price range")
    print("4. Show all products")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_product(products)
    elif choice == '2':
        update_price(products)
    elif choice == '3':
        find_in_range(products)
    elif choice == '4':
        print(products)
    elif choice == '5':
        break
    else:
        print("Invalid choice!")
