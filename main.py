import datetime
import json
import os
import pandas as pd
from params import *
import requests

url_api = 'https://www.data.gouv.fr/api/1/datasets/5e5d89c28b4c410f100c3242/resources/'
resource_XLSX = '352b3cea-21d7-4cfc-87d3-dddab11b4021'
resource_CSV = 'bab27c3e-5620-47b2-8ed8-797c8192d905'

url_efs = 'https://api.efs.sante.fr/carto-api/v2/SamplingCollection/SearchNearPoint?CenterLatitude=48.85&CenterLongitude=2.35&DiameterLatitude=180&DiameterLongitude=360&UserLatitude=48.85&UserLongitude=2.35&Limit=1000000'


def add_prefix(dictionnary, prefix):
    return {prefix + key: value for key, value in dictionnary.items()}


def build_database(results):
    collections = []
    for result in results:
        location = result.copy()
        del location['collections']
        del location['distance']
        location = add_prefix(location, 'location_')
        for collection in result['collections']:
            collection['date'] = collection['date'][0:10]
            collection = add_prefix(collection, 'collection_')
            row = location.copy()
            row.update(collection)
            collections.append(row)
    return pd.DataFrame(collections)


def upload_file(local_name, resource_id):
    print('Uploading file')
    headers = {
        'X-API-KEY': X_API_KEY
    }
    response = requests.post(url_api + resource_id + '/upload/', files={'file': open(local_name, 'rb')}, headers=headers)
    print('Uploaded file')
    print('Uploading metadata')
    headers = {
        'Content-Type': 'application/json',
        'X-API-KEY': X_API_KEY
    }
    old_data = response.json()
    data = { 
        'published': old_data['last_modified']
    }
    response = requests.put(url_api + resource_id + '/', data=json.dumps(data), headers=headers)
    print('Uploaded metadata')

    
def save_and_upload(database):
    database.to_csv('collections.csv', index=False, encoding='UTF-8')
    with pd.ExcelWriter('collections.xlsx') as writer:
        database.to_excel(writer, sheet_name='collections', index=False)
    upload_file('collections.csv', resource_CSV)
    upload_file('collections.xlsx', resource_XLSX)

print('Downloading data')
response = requests.get(url_efs)
if response.status_code == 200:
    print('Request successful')
    db = build_database(response.json())
    save_and_upload(db)
else:
    print('Request failed')
