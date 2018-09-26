#!/usr/bin/python

import socket 
import json

data = json.loads(open('file.json').read())
host=data["host"]
port=data["port"]
print (data["host"])

sock = socket.socket()
#host = 'localhost'
#port = 12345
temperature="24"
boiler="Boiler enabled"

sock.bind((host,port))

sock.listen(1)

while True:
	conn,addr = sock.accept()
	print ('connected:', addr)
	command = conn.recv(1024)
	command=bytes.decode(command)
	print(command)
	if (command=='1'):
		print(1)
		conn.send(temperature.encode('utf-8'))
	elif (command=='2'):
		print(2)
		conn.send(boiler.encode('utf-8'))
	elif (command=='3'):
		if(boiler=='Boiler enabled'):
			boiler='The boiler is switched off'
			conn.send("The boiler is switched off".encode('utf-8'))
		else:
			boiler='Boiler enabled'
			conn.send("Boiler enabled".encode('utf-8'))

conn.close()
