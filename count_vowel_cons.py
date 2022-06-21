vowels = ['a','e','i','o','u']
user = input().lower().replace(' ','')

v_count = 0
c_count = 0
for i in user:
    if i in vowels:
        v_count += 1
    else:
        c_count += 1
print(v_count)
print(c_count)