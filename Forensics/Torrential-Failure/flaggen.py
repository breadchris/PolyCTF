flag = "flag{W3ll_th4t_wuz_EZ}"

with open('flag.txt', 'w') as f:
    for i in xrange(10000):
        f.write(flag + '\n')
