#!/usr/bin/python

import requests
from threading import Thread
import sys
import time
import getopt
from requests.auth import HTTPDigestAuth

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