food_items = [("Pizza", 8.99),("Burger", 5.49),("Sushi", 12.75),("Pasta", 7.25),("Salad", 4.50)]

sorted_food = sorted(food_items, key=lambda item: item[1], reverse=True)

print("Food items sorted by price (high to low):")
for food, price in sorted_food:
    print(f"{food}: ${price:.2f}")