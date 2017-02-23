import re

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
#text = handle.read()

hourcount = dict()
for line in handle:
    line = line.rstrip()
    if line == '' : continue
    words = line.split()
    if words == [] : continue
    if len(words) < 1: continue
    if words[0] != 'From': continue
    hour = words[5]
    hour = hour[:2]    
    if hour not in hourcount:
        hourcount[hour] = 1
    else:
        hourcount[hour] = hourcount.get(hour,0) + 1
temp = list()
for a, b in hourcount.items():
     temp.append( (a, b) )
temp.sort()
for a, b in temp[:]:
    print a, b