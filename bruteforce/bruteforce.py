#!/usr/bin/python
import requests
page_url = "http://192.168.0.20/dvwa/login.php"
username = input(" enter User Name for speecified page : ")

with open("passwordlist.txt", "r") as passwords:
    bruteforce(username, page_url)
