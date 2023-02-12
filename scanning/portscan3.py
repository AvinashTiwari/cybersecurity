#!/usr/bin/python

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)
'''
host = "192.168.0.5"
port = 443
'''
host =  input("[*] Enter The Host to Scan: ")
'''
port = int(input("[*] Enter The Port to Scan: "))
'''
def portscanner(port):
        if sock.connect_ex((host,port)):
                print(colored("Port %d is  closed"%(port), 'red'))
        else:
                print(colored("Port %d is opened"%(port),'green'))

for port in range(1,100):
	portscanner(port)

