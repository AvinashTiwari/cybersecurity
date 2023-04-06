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
                    


