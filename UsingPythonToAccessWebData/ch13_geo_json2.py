# coding: utf-8
# this code runs in Python 3.4.3 env

import urllib.request
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    uni = input('Enter university: ')
    if len(uni) < 1 : uni = 'University of Utah'
    #	address = address.decode('utf8')
    print(uni)

    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': uni})

    print('Retrieving', url)
    with urllib.request.urlopen(url) as uh:
        data = uh.read()
    print('Retrieved',len(data),'characters')

    try:
        js = json.loads(data.decode())
    except:
        js = None
        print(json.dumps(js, indent=4))
    
    if "status" not in js or js['status'] != 'OK':
        print ('=====Failure To Retrieve=====')
        continue    
    place_id = js["results"][0]["place_id"]
    print(place_id)
    
