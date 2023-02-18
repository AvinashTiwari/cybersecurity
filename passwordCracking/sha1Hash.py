#!/usr/bin/python

from urllib.request import urlopen
import hashlib

sha1hash = input("[*] enter Sha1 has Value : ")
passlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')
for i in passlist.split('\n'):
	hashguess = hashlib.sha1(bytes(i,'utf-8')).hexdigest()
	if hashguess == sha1hash:
		print("[+] The Password is : " +str(i))
		quit()
	else:
		print("[-] Password Guess" + str(i) + " does not match next in List")

print("password not in pasword list")

