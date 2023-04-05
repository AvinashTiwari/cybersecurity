#!/usr/bin/python

import requests

def request(full_url):
    try:
        return requests.get("http://"+full_url)
    except requests.exceptions.ConnectionError:
        print("exception ocuured " + "http://"+full_url)
        pass

target_url = input("[*] Enter Target Url: ")
file = open("subdomains.txt", "r") 
for line in file:
    word = line.strip()
    full_url = word +"." + target_url 
    response = request(full_url)
    if response:
        print("[+] Discovered SubDomian at this link " + full_url)