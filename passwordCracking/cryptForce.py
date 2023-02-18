#!/usr/bin/python
import crypt

def CrackPass(cryptWord):
	salt = cryptWord[0:2]
	dictonary = open('dict.txt','r')
	for word in dictonary.readlines():
		word = word.strip('\n')
		cryptpass = crypt.crypt(word,salt)
		if(cryptWord == cryptpass):
			print("[+] Found Password: " + word)
			return 
	print("[-] Password Not found")
	return


def main():
	passfile = open('passsalt.txt','r')
	for line in passfile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptWord = line.split(':')[1].strip(' ').strip('\n')
			print("[*] Cracking Password for: "  + user)
			CrackPass(cryptWord)
main()
