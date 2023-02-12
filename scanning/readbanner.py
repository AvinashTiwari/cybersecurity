#!/usr/bin/python

import socket

def returnBanner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024)
		return banner
	except:
		return 

def main():
	ip = input("[*] Enter Target IP: ")
	for x in range(1,100):
		'''
		port =	22
		ip = "192.168.0.20"
		'''
		port = x
		banner = returnBanner(ip,port)
		if banner:
			print("[+]"  + ip +"/"+ str(port)  +  ":" +  banner.decode("ISO-8859-1").strip('/n'))
main()
