try:
    name = input()
    if len(name) < 4:
        raise Exception()
    print("Account Created")
except:
    print("Invalid Name")
    