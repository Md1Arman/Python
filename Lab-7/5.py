# 05. Create two dictionaries – one containing grocery items and their prices and another containing grocery items and quantity purchased. By using the values from these two dictionaries compute the total bill.

def create_price_quantity_dict(num_entries):
    prices = {}
    quantities = {}

    for i in range(num_entries):
        item = input(f"Enter name of grocery item {i + 1}: ")
        price = float(input(f"Enter price of {item}: "))
        quantity = int(input(f"Enter quantity of {item}: "))
        prices[item] = price
        quantities[item] = quantity

    return prices, quantities

def count_total_bill(prices, quantities):
    total_bill = 0

    for item, quantity in quantities.items():
        if item in prices:
            total_bill += prices[item] * quantity
        else:
            print(f"Warning: '{item}' not found in the price dictionary.")

    return total_bill

# Main code
num_entries = int(input("Enter the number of grocery items you want to buy: "))
grocery_prices, grocery_quantities = create_price_quantity_dict(num_entries)

print("\nDictionary of Grocery items and their prices:")
print(grocery_prices)

print("\nDictionary of Grocery items and their quantities:")
print(grocery_quantities)

print("\nTotal bill: ₹", count_total_bill(grocery_prices, grocery_quantities))
