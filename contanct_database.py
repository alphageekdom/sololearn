import re

# phone_num = input()
# pattern = r"00"
# match = re.match(pattern, phone_num)
# if match:
#     print(re.sub(pattern, "+", phone_num, count=1))
# else:
#     print(phone_num)

phone_num = input()
phone_num = re.sub("^00", "+", phone_num)
print(phone_num)