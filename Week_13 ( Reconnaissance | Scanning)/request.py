#!/usr/bin/env python3

import requests

url='https://docs.google.com/forms/u/0/d/e/1FAIpQLSd_y2jhFAzufGJBG7PEAtXRSHhYrK_SWrQAQAT5Gk2zWC5uRA/formResponse'

form_data = {'entry.2005620554':'This is a test'}

r = requests.post(url, data=form_data)
