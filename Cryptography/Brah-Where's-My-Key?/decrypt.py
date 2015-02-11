'''
VeryLongKeyYouWillNeverGuess
Nice job! You solved the challenge. Here is your flag: flag{3ncrypt_your_sh!t_y0}
'''

plain = open("msg001", "rb")
enc1  = open("msg001.enc", "rb")
enc2  = open("msg002.enc", "r")

plain_data1 = plain.read()
enc_data1 = enc1.read()

tmp = 0
key = ''
for i in range(0, len(plain_data1)):
    x = ((ord(enc_data1[i]) - (i*i) - ord(plain_data1[i])) & 0xff) ^ tmp
    key += chr(x)
    tmp = ord(plain_data1[i])

enc_data2 = enc2.read()

key = key[:-2]
print key

t = 0
out = ''
for i in range(0, len(enc_data2)):
    c = (ord(enc_data2[i]) - (ord(key[i % len(key)]) ^ t) - i*i) & 0xff
    out += chr(c)
    t = c

print out
