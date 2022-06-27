def spell(txt):
    size = len(txt)
    if size == 0:
        return
    else:
        last_char = txt[size-1]
        print(last_char)
        spell(txt[0:size-1])


txt = input()
spell(txt)
