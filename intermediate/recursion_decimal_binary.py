def convert(num):
    if num == 0:
        return 0
    else:
        return (num % 2 + 10 * convert(num // 2))

print(convert(156))