# This code is for Python 3.4.3
# coding: utf-8
import urllib.request
import json

serviceurl = 'http://python-data.dr-chuck.net/comments_173608.json'
count = 0

while True:
    url = input('Enter url: ')
    if len(url) < 1 : url = serviceurl
    print(url, type(url))

    print('Retrieving', url)
    with urllib.request.urlopen(url) as uh:
        data = uh.read()
    print('Retrieved',len(data),'characters', 'data Type is:', type(data))

    try:
        js = json.loads(data.decode())
    except:
        js = None
#    print(json.dumps(js, indent=4), '\n')
   
    for element in js["comments"]:
#        print(element)
        count = count + element["count"]
    print ('Count:', count)
"""""" 
