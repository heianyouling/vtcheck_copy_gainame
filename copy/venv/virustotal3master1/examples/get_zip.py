import os
import time
import sys
sys.path.append('..')
import virustotal3.enterprise

#API_KEY = os.environ['VT_API']

vt = virustotal3.enterprise.ZipFiles('0703c8673d85549f143f9bc0e845ba9d255bfc10a9c7140923d4a63651807a83')

data = {
        "data": {
            "password": "infected",
            "hashes":[
            "D0CEB18272966AB62B8EDFF100E9B4A6A3CB5DC0F2A32B2B18721FEA2D9C09A5"]
            }
        }

# Create a zip file
results = vt.create_zip(data)

# Get the ID
zip_id = results['data']['id']
print(zip_id)

# Check the status
info = vt.info_zip(zip_id)
status = info['data']['attributes']['status']

while not status == 'finished':
    time.sleep(3)
    info = vt.info_zip(zip_id)
    status = info['data']['attributes']['status']
    print('Status: ' + status)

print('Status: Downloading...')
vt.get_zip(zip_id, './')
print('Status: Done!')