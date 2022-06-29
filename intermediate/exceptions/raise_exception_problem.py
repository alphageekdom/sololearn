tweet = input()

try:
    if len(tweet) > 42:
        raise Exception()
except:
    print("Error")
else:
    print("Posted")
