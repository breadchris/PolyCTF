from random import randint
from string import printable

flag = "flag{there_was_a_lot_of_crap_in_there}"

i = 0
with open("flag.crap", "wb") as f:
    for x in xrange(1024):
        if randint(0, 1024) < len(flag):
            if i == len(flag):
                break
            f.write(flag[i])
            i += 1
        else:
            x = randint(0, 255)
            while chr(x) in printable:
                x = randint(0, 255)
            f.write(chr(x))
