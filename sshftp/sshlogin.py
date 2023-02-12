#!/usr/bin/python

import pexpect
PROMPT = ['# ', '>>> ', '> ', '\$ ']

def send_command(child, command):
	child.sendline(command)
	child.expect(PROMPT)
	print (child.before)

def connect(user, host,password):
	print("Enterning Connect")
	ssh_newkey = 'Are you sure you want to continue connecting (yes/no/[fingerprint])? '
	conStr = 'ssh -oHostKeyAlgorithms=+ssh-rsa ' + user +  '@'  + host
	child = pexpect.spawn(conStr)
	ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:' ])
	print(conStr)
	print("Before ret given" + str(ret)  + str(child.after) )
	if ret == 0:
		print('[-] Error Connecting')
	if ret == 2:
		print("Value of ret is 2")
		child.sendline('yes')
		ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
		if  ret == 0:
			print('[-] Error Connecting')
			return
		child.sendline(password)
		child.expect(PROMPT)
		print("Value of ret " +  str(ret) )
		return child

def main():
	host = '192.168.0.20'
	user = 'msfadmin'
	password = 'msfadmin'
	'''
	host = input("Enter Hostname or Ipaddress")
	user = input("Enter Username")
	password = input("Enter password")
	'''
	child = connect(user, host, password)
	'''
	send_command(child,'cat /etc/shadow | grep root;ps')
	'''
	send_command(child,'ls')
main()
