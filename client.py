#!/usr/bin/python

import socket 

sock = socket.socket()
host = 'localhost'
port = 60000

sock.connect(('localhost', port))


print ("Choose a command :")
print ("1 : Check the temperature")
print ("2 : Check the condition of the boiler")
print ("3 : Turn on / off boiler")

command = input("Command : ")
command = str.encode(command,'utf-8')
sock.send(command)
res = sock.recv(1024)
res = bytes.decode(res,'utf-8')

print (res)

sock.close   