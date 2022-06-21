file = open("./books.txt", "r")

for title in file:
    name = title.replace("\n", "")
    result = title[0] + str(len(name))
    print(result)
file.close()