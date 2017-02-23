# coding: utf-8
# this code runs in Python 2.7 env

import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : address = 'Петрозаводск'
    #	address = address.decode('utf8')
    print address

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
#    print 'url:',url
#    print data

    try:
        js = json.loads(str(data))
    except:
        js = None
    if 'status' not in js or js['status'] != 'OK':
        print '=====Failure To Retrieve====='
#        print data
        continue
#    print json.dumps(js, indent=4)
     
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat:',lat,'lng:',lng
    location = js["results"][0]["formatted_address"]
    print location

