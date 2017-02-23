valuelist = []
while True:
    val = raw_input('Enter value:')
    if val == 'done': break
    valuelist.append(val)
print 'Max:', max(valuelist)
print 'Min:', min(valuelist)

#list = [1,2,3,4,5,6,7,8,9,0]
#def chop(list):
#    list = list[1:len(list)-1]
#    
#def middle(list):
#    list = list[1:len(list)-1]
#    return list
#
#print chop(list)

#fname = raw_input('Enter file name: ')
#if len(fname) == 0: 
#	fname = 'mbox-short.txt'
#fh = open(fname)
#for line in fh:
#    line = line.rstrip()
#    if line == '' : continue
#    words = line.split()
#    if words == [] : continue
#    if len(words) < 1: continue
#    if words[0] != 'From': continue
#    print words[0]


#fname = raw_input('Enter file name: ')
#if len(fname) == 0: 
#	fname = 'mbox-short.txt'
#fh = open(fname)		
#count = 0
#emails = list()
#for line in fh:
#	if line.startswith('From '):
#		line = line.strip()
#		lst = line.split()
#		emails.append(lst[1])
#for i in emails:
#	print emails[count]
#	count = count + 1
#print 'There were', count, 'lines in the file with From as the first word'


#fname = raw_input('Enter file name: ')
#if len(fname) == 0: 
#	fname = 'romeo.txt'
#fh = open(fname)
#words = list()
#lst = list()
#for line in fh:
#	words = line.split()
#	for i in words:
#		if i not in lst:
#			lst.append(i)
#lst.sort()
#print lst