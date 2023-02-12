#!/usr/bin/python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)
'''
host = "192.168.0.5"
port = 443
'''
host =  input("[*] Enter The Host to Scan: ")
port = int(input("[*] Enter The Port to Scan: "))

def portscanner(port):
        if sock.connect_ex((host,port)):
                print("Port %d is  closed"%(port))
        else:
                print("Port %d is opened"%(port))

portscanner(port)
