# class Pizza:
    
#     def __init__(self, toppings):
#         self.toppings = toppings
    
#     @staticmethod
#     def validate_topping(topping):
#         if topping == "pineapple":
#             raise ValueError("No pineapples!")
#         else:
#             return True


# ingredients = ["cheese", "onions", "spam"]
# if all(Pizza.validate_topping(i) for i in ingredients):
#     pizza = Pizza(ingredients)

class Calculator():
    
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    @staticmethod
    def add(n1, n2):
        return (n1 + n2)

n1 = int(input())
n2 = int(input())

print(Calculator.add(n1, n2))