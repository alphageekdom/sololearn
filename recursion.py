# def convert(num):
#     if num < 1:
#         return 0
#     return (num % 2 + 10 * convert(num // 2))


# num = int(input())
# print(convert(num))

# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x - 1)

# print(factorial(5))

def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

print(is_odd(77))