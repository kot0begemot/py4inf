"""
9.4 Write a program to read through the mbox-short.txt and figure out 
who has the sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines
as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address 
to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary 
using a maximum loop to find the most prolific committer.
Desired Output: cwen@iupui.edu 5
"""

#ver2
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
#text = handle.read()

ecount = dict()
for line in handle:
    line = line.rstrip()
    if line == '' : continue
    words = line.split()
    if words == [] : continue
    if len(words) < 1: continue
    if words[0] != 'From': continue
    hour = words[5]
    hour = hour[:2]    
    if hour not in ecount:
        ecount[hour] = 1
    else:
        ecount[hour] = ecount.get(hour,0) + 1
temp = list()
for a, b in ecount.items():
     temp.append( (b, a) )
temp.sort(reverse=True)
for a, b in temp[:3]:
    print b, a

#shorter version:
# c = {'a':b, 'b':1, 'c':22}
#print sorted( [ (v,k) for k,v in c.items() ] )
#[(1, 'b'), (10, 'a'), (22, 'c')]

#for key in ecount:
#    print key, ecount[key]
#print 'maximum:', max(ecount.values())


#ver1
#name = raw_input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"
#handle = open(name)
#text = handle.read()
#words = text.split()
#
#emailcount = dict()
#i = 0
#for word in words:
#    if word == 'From':
#        emailcount[words[i+1]] = emailcount.get(words[i+1],0) + 1
#        print words[i+1], emailcount[words[i+1]]
#    i = i + 1
#    
#spamercount = None
#spamername = None
#for email,count in emailcount.items():
#    if spamercount is None or count > spamercount:
#        spamercount = count
#        spamername = email
#print spamername, spamercount
