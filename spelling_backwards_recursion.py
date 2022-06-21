def spell(txt):
    if len(txt) == 0:
        return 0
    else:
        return txt[::-1]

txt = input()
print(spell(txt))