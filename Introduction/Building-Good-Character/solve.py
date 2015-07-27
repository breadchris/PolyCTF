import string

with open("flag.crap", "r") as f:
    flag = ""
    x = f.read()
    for c in x:
        if c in string.printable:
            flag += c
    print flag
