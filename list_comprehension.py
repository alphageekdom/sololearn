# result = [i*2 for i in range(10)]
# print(result)

# for i in range(10):
#     print(i*2)

x = int(input())

result = [i for i in range(x) if i % 3 == 0 and i % 5 ==0]
print(result)