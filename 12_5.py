import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

data = mysock.recv(512)
message = data.decode()
header_end_pos = message.find('\r\n\r\n') + 4   #Finds the end of header
                                            #Adds four to exclude:'\r\n\r\n'
print(message[header_end_pos:])
while True:                                 #Header in the first data only
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
