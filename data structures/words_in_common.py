s1 = input()
s2 = input()

text1 = set(s1.split())
text2 = set(s2.split())
res = text1 & text2
print(len(text1 & text2)),