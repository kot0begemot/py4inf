import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
if len(url) < 1 : url = "http://profi.ru"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve a list of the anchor tags
# Each tag is a dict of HTML attributes

tags = soup('a')
for tag in tags:
    print tag.get('href', None)
    

