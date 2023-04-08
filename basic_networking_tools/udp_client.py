#!/usr/bin/python
print('-- UDP Client --')
import socket

target_host = "127.0.0.1"
target_port = 9997

# create client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind((target_host, target_port))

# send data
client.sendto(b"AAABBBCCC", (target_host, target_port))

# recieve data
data, addr = client.recvfrom(4096)

print(data)
client.close()