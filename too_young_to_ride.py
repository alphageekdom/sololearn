# ages = []
# i = 0

# while i < 3:
#     age = int(input())
#     ages.append(age)
#     i += 1
#     if age < 16:
#         print("Too young!")
#         break

# else:
#     print("Get ready!")

for i in range(10):
    try:
        if 10/i == 2.0:
            break
    except ZeroDivisionError:
        print(1)
    else:
        print(2)