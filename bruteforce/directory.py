#!/usr/bin/python

import requests

def request(full_url):
    try:
        return requests.get("http://"+full_url)
    except requests.exceptions.ConnectionError:
        print("exception ocuured")
        pass

target_url = input("[*] Enter Target Url: ")
file = open("common.txt", "r") 
for line in file:
    word = line.strip()
    full_url = target_url + "/" + word
    response = request(full_url)
    if response:
        print("[+] Discovered Directoy at this link " + full_url)