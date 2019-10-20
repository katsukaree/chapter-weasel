#!/usr/bin/env python3

import urllib.request
import base64
from levels_credentials import credentials

level_url = credentials[1]["url"]
level_username = credentials[1]["level"]
level_password = credentials[1]["password"]

next_level_username = credentials[2]["level"]

credentials = "%s:%s" % (level_username, level_password)
auth_creds = base64.b64encode(credentials.encode("ascii"))

req = urllib.request.Request(level_url)
req.add_header("Authorization", "Basic %s" % auth_creds.decode("ascii"))

with urllib.request.urlopen(req) as response:
    data = response.read()
    strings = data.split()
    next_password = strings[strings.index(next_level_username.encode("ascii")) + 2]

print(next_password.decode("ascii"))
