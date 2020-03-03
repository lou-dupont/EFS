import datetime
import json
import os
from params import *
import requests

# Minimum valid size of 100 kb (to avoid overiding a previous valid file with a new empty one)
MIN_VALID_SIZE = 100 * 1000

url_source = "https://dondesang.efs.sante.fr/get-collects-ajax?neLon=180&neLat=90&swLon=-90&swLat=-180"
url_api = "https://www.data.gouv.fr/api/1/datasets/5e5d89c28b4c410f100c3242/resources/205fae5e-e0b2-43f1-a198-2cd9dfd7a93d/"

temp_json = 'current-collects.json'

print("Downloading data")
collects_json = requests.get(url_source).content
with open(temp_json, 'wb') as temp_file:
    temp_file.write(collects_json)

if len(collects_json) > MIN_VALID_SIZE:

    print("Uploading file")
    headers = {
        "X-API-KEY": X_API_KEY
    }
    response = requests.post(url_api + "upload/", files={'file': open(temp_json, 'rb')}, headers=headers)
    os.remove(temp_json)
    print(response.content)

    print("Uploading metadata")
    headers = {
        "Content-Type": "application/json",
        "X-API-KEY": X_API_KEY
    }
    old_data = response.json()
    data = { 
        "published": old_data["last_modified"]
    }
    response = requests.put(url_api, data=json.dumps(data), headers=headers)
    print(response.content)
