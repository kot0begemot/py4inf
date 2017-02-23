# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
if len(url) < 1 : url = "http://python-data.dr-chuck.net/comments_173607.html"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the span tags
tags = soup('span')
total = list()
for tag in tags:
    # Look at the parts of a tag
#   print 'SPAN:',tag.contents[0]
    total.append(int(tag.contents[0]))
print 'result:', sum(total)
