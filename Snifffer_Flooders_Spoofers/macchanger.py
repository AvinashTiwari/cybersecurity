#!/usr/bin/python

import subprocess
def change_mac_address(interface,mac):
	print(interface + "==" + mac)
	subprocess.call(["ifconfig" , interface , "down"],shell=True)
	subprocess.call(["ifconfig" , interface , "hw", "ether" , mac], shell=True)
	subprocess.call(["ifconfig", interface , "up"], shell=True)

def main():
	interface = input("[*] Enter Interface to Chnage Mac Address on: ")
	new_mac_address = input("[*] Enter Mac Address to change to: ")
	before_change = subprocess.call(["ifconfig" , interface],shell=True)
	change_mac_address(interface,new_mac_address)
	after_change = subprocess.call(["ifconfig" , interface], shell=True)
	print(before_change)
	print(after_change)
	if before_change == after_change:
		print("[!!] Failed to change mac address to: " + new_mac_address)
	else:
		print("[+] Mac Address Chnaged To: " + new_mac_address + " On Interface" + interface)
main()
