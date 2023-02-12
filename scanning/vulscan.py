#!/usr/bin/python

import socket
import os
import sys
from termcolor import colored, cprint

def retBanner(ip,port):
	try:
		print("Call happened from retBanner " + ip  + ":" +  str(port))
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024)
	except Exception as e:
		print(e)
		print("error ocuured in retBanner")
		return
def checkVulns(banner, filename):
	f = open(filename, "r")
	for line in f.readlines():
		print("reading Line")
		if line.strip("\n") in banner:
			print("[+] server is vulnerable : " +  banner.strip("\n"))

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print ("[-] File doesnot exist!")
			exit(0)
		if not os.access(filename, os.R_OK):
			print("[-] Access denied!")
			exit(0)
	else:
		print('[-] Usage : ' +  str(sys.argv[0])  + "Vul file name")
		exit(0)
	portlist = [21,22,25,80,110,443,445]
	for x in range(1,255):
		ip = "192.168.0."+ str(x)
		print("[+]" + ip)
		for port in portlist:
			print("[+] " + str(port))
			banner = retBanner(ip, port)
			if banner:
				print("[+]" +  ip  +  "/" + str(port) + " : " + banner.decode("ISO-8859-1"))
				checkVulns(banner, filename)
main()
