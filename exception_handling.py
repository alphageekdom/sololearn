coffee = ["Cafe Latte", "Caffe Americano", "Esperesso", "Cappuccino", "Macchiato"]

choice = int(input())

try:
    print(coffee[choice])

except:
    print("Invalid number")

finally:
    print("Have a good day")