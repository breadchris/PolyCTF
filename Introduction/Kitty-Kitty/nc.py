import socket

host = ''
port = 9001
backlog = 5
size = 1024
flag = "flag{you_pet_the_cat!}"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
while 1:
    client, address = s.accept()
    client.send(flag)
    client.close() 
