def withdraw(amount):
    print(str(amount) + " withdrawn!")

n = input()
try:
    int(n)
    withdraw(n)
except ValueError:
    print("Please enter a number")