"""The basic outline of this problem is to read the file, 
look for integers using the re.findall(), looking for a regular expression of '[0-9]+' 
and then converting the extracted strings to integers and summing up the integers.
"""

import re

name = raw_input("Enter file:")
if len(name) < 1 : name = "regex_sum_173602.txt"
handle = open(name)
#text = handle.read()

count = list()
s = list()
for line in handle:
    line = line.rstrip()
    if line == '' : continue
    words = line.split()
    if words == [] : continue
    if len(words) < 1: continue
    count = re.findall('[0-9]+', line)
    if count !=[]:
        s = s + [int(x) for x in count]
print "s=", sum(s)

