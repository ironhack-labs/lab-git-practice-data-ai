#Program that manages customer orders and inventory by Cecilia Betek
# 1. Define a list called products
products = ["t-shirt", "mug", "hat", "book", "keychain"]
# 2. Create an empty dictionary
inventory = {}
# 3.
inventory = {"t-shirt":20, "mug": 5, "hat":15, "book": 24, "keychain": 19}
#4
for product in products:
    quantity = int(input(f"Enter quantity for {product}: "))
    inventory[product] = quantity
#4
customer_orders = set()
#5
print("\nAvailable products:", products)
for i in range(3):
    order = input(f"Enter product #{i+1} to order: ").lower()
    if order in products:
        customer_orders.add(order)
    else:
        print("Invalid product, please choose from the list.")
#6
print("\nCustomer Orders:", customer_orders)
#7
total_products_ordered = len(customer_orders)
percentage_ordered = (total_products_ordered / len(products)) * 100
#8
order_status = (total_products_ordered, percentage_ordered)
#9
print("\nOrder Statistics:")
print("Total Products Ordered:", order_status[0])
print("Percentage of Products Ordered: {:.2f}%".format(order_status[1]))
# Step 10
for product in customer_orders:
    if inventory[product] > 0:
        inventory[product] -= 1

# Step 11
print("\nUpdated Inventory:")
for product, quantity in inventory.items():
    print(f"{product}: {quantity}")