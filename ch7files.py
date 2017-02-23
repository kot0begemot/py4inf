fout = open('output/output.txt', 'w')
print fout
line1 = "This here's the wattle,\n"
fout.write(line1)
line2 = 'the emblem of our land.\n'
fout.write(line2)
fout.close()

s = '1 2\t 3\n 4'
print s
print repr(s)

# Use the file name mbox-short.txt as the file name
#try:
#    fname = raw_input("Enter file name: ")
#    fh = open(fname)
#except:
#    print "Filename incorrect."
#    exit()
#count = 0
#total = 0
#for line in fh:
#    if not line.startswith("X-DSPAM-Confidence:") : 
#        continue
#    line = line.strip()
#    count = count + 1
#    colpos = line.find(":")
#    number = float(line[colpos + 1:])
#    total = total + number
#averageXSpam = total / count
#print "Average spam confidence:", averageXSpam

#try:
#    fname = raw_input("Enter file name: ")
#    fh = open(fname)
#except:
#    print "Filename incorrect."
#    exit()
#for line in fh:
#    line = line.strip()
#    line = line.upper()
#    print line