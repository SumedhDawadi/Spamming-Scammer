#!/usr/bin/env python3

print(""" \33

 
████▓▓▓▓▓▓▓█████╬╬╬╬╬╬████╬╬╬╬╬╬╬╬╬╬╬╬██
███▓▓▓▓▓▓▓▓▓▓▓██╬╬╬╬╬╬██╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓▓▓▓▓▓▓▓▓▓▓██╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
███▓▓▓███████▓▓▓███╬╬╬╬╬╬█████████╬╬╬╬██
███▓▓██████████▓▓██╬╬╬╬╬████████╬╬╬╬╬╬██
███▓▓▓▓▓▓▓▓▓▓▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓▓▓▓▓▓▓▓▓▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
█████▓▓▓▓▓▓▓▓▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
█████▓▓▓▓▓▓▓▓█▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
█████▓▓▓▓▓▓▓██▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
█████▓▓▓▓▓████▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓▓▓▓▓▓██▓▓▓▓███╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓▓█▓▓▓▓▓▓▓▓▓███╬╬╬╬╬╬╬╬╬╬╬╬██╬╬╬╬███
█████▓██▓▓▓▓▓▓▓▓▓██████╬╬╬╬╬╬╬██╬╬╬╬╬███
█████▓▓█████▓▓▓████╬████╬╬╬████╬╬╬╬╬╬███
██████▓▓▓▓████████╬╬╬████████╬╬╬╬╬╬╬████
███████▓▓▓▓▓▓▓▓▓█████████╬╬╬╬╬╬╬╬╬╬╬████
███████▓▓▓▓▓▓▓▓███╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬█████
████████▓▓▓▓▓▓▓▓████╬╬╬╬╬╬╬╬╬╬╬╬╬╬██████
█████████▓▓▓▓▓▓▓▓▓███╬╬╬╬╬╬╬╬╬╬╬╬███████
██████████▓▓▓▓▓▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬████████
███████████▓▓▓▓▓▓▓███╬╬╬╬╬╬╬╬╬╬█████████
 Spamming-Scammer
 AUTHOR : @SUMEDH DAWADI                                                                              
""")

import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))


#### Make sure you change the url#############


url = ' http://127.0.0.1/login.html'
names = json.loads(open('names.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	username = name.lower() + name_extra + '@gmail.com'
	password = ''.join(random.choice(chars) for i in range(8))

	requests.post(url, allow_redirects=False, data={
		'auid2yjauysd2uasdasdasd': username,
		'kjauysd6sAJSDhyui2yasd': password
	})

	print ('sending username %s and password %s' % (username, password))
    

     