#!/usr/bin/python

import ftplib

def annonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymus;,anonymus')
		print("[*] "  + Hostname +" FRP Anonymus logon Succceded.")
		ftp.quit()
		return True
	except e:
		print("[-]" + hostname + " FTP Anonymus Login failed.")


host = input("Enter The Ip Address : ")
annonLogin(host)
