#!/usr/bin/python3

import requests

url='https://docs.google.com/forms/u/0/d/e/1FAIpQLSdiMHViuoPlW3UujN2b0M3xiT81aKGeEp779j46XlD58PzZ1A/formResponse'

form_data = {'entry.2005620554':'This is a test'}

r = requests.post(url, data=form_data)
