#!/usr/bin/env python3

import requests
import base64
import re
from levels_credentials import credentials

level_url = credentials[8]["url"]
level_username = credentials[8]["level"]
level_password = credentials[8]["password"]

next_level_url = credentials[9]["url"]
next_level_username = credentials[9]["level"]

credentials = "%s:%s" % (level_username, level_password)
auth_creds = base64.b64encode(credentials.encode("ascii"))
heads = {"Authorization": "Basic %s" % auth_creds.decode("ascii"), "Referer": next_level_url}

secret_url = level_url + "/includes/secret.inc"

secret_response = requests.get(secret_url, headers=heads)

secret_data = "3d3d516343746d4d6d6c315669563362"
secret_string_rev = bytes.fromhex(secret_data)
secret_strings = secret_string_rev[::-1]
secret_enc = base64.b64decode(secret_strings)
secret = secret_enc.decode("ascii")

post_data = {"secret": secret, "submit":"Submit+Query"}
response = requests.post(level_url, headers=heads, data=post_data)

data = response.text
strings = re.split('\n|:|\s|<|>', data)
next_password = strings[strings.index(next_level_username) + 2]

print(next_password)
