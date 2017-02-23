# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
import re
from BeautifulSoup import *

url = raw_input('Enter : ')
if len(url) < 1 : url = "http://python-data.dr-chuck.net/known_by_Helena.html"

count = 7
position = 17
taglist = list()

for step in range(count):
    # Retrieve all of the anchor tags and make list of strings
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    anchortags = soup('a')
    for tag in anchortags:
        taglist.append(tag.get('href', None))
    
    url = taglist[position]
    del taglist[:]
    print url
print re.findall('(?<=by_)(.*)(?=.html)', url)

    
