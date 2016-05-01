# -*- coding: utf-8 -*-

import socket

target_host = "0.0.0.0"
target_port = 9999

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect server
client.connect((target_host, target_port))

# send data
client.send("ABCDEF\r\n\r\n")

# receive data
response = client.recv(4096)

print response
