menu = ["Fries", "Sandwich", "Cheeseburger", "Coffee", "Soda"]

try:
    n = int(input())
    print(menu[n])
    print("Thanks for your order")
except (IndexError, ValueError):
    print("Item not found")
