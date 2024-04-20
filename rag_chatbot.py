#
# step 1 get  documents
#
import requests
url = 'http:/xxxx/text_demo"
resp = requests.get(f"{url}/mydoc.txt"}
text = resp.text if resp.status_code == 200 else ""

import os
if.os.path.exists("mydoc.txt"):
    with.open("mydoc.txt", "r", encoding=utf8") as file:
       text = ""
       for line in file.readLines():
           text += line

#
# step 2 embedding
#
