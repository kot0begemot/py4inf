# Parces XML from URL by tag
import urllib
import re
import xml.etree.ElementTree as ET
sum_count = 0

while True:
    url = raw_input('Enter URL: ')
    if len(url) < 1 : url = 'http://python-data.dr-chuck.net/comments_173604.xml'

    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    tree = ET.fromstring(data)
    counts = tree.findall('.//count')
    for count in counts:
        sum_count += int(count.text)
                
    print sum_count
    break
#    


