# def isPrime(x):
#     if x < 2:
#         return False
#     elif x == 2:
#         return True
#     for n in range(2, x):
#         if x % n == 0:
#             return False
#     return True

# def primeGenerator(a, b):
#     for n in range(a, b):
#         if isPrime(n):
#             yield n

# f = int(input())
# t = int(input())
# print(list(primeGenerator(f, t)))

# def countdown():
#     i = 5
#     while i > 0:
#         yield i
#         i -= 1

# for i in countdown():
#     print(i)

# def infinite_sevens():
#     while True:
#         yield 7

# for i in infinite_sevens():
#     print(i)

# def numbers(x):
#     for i in range(x):
#         if i % 2 == 0:
#             yield i

# print(list(numbers(11)))

# text = "This is some text"

# def words():
#     for word in text.split():
#         yield word
        

# print(list(words()))