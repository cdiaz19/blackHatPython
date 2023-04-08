#!/usr/bin/python
print('-- TCP Client --')

import socket

target_host = "www.google.com"
target_port = 80

# # socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# #connet the client
client.connect((target_host, target_port))

# # send data
client.send(b"GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n")

# #receive data
response = client.recv(4096)
print(response)

# # close connection
client.close()
