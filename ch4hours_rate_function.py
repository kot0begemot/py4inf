try:
    inp = raw_input("Enter Hours:")
    h = float(inp)
    inp = raw_input("Enter Rate:")
    r = float(inp)
except:
    print "Please, enter numeric"
    quit()
print h, r
if h <= 40.00 :
    overpay = 0
else :
    overpay = h - 40
    h = 40
def computepay(h,r):
    pay = h * r + overpay * r * 1.50
    return(pay)
p = computepay(h,r)
print 'Pay:', p

#hours = raw_input("Hours?:")
#rate = raw_input("Rate?:")
#pay = float(hours) * float(rate)
#print "Pay:",pay,"$"

#x = int(98.6)
#print x

#inp = raw_input("Hours?:")
#hours = float(inp)
#inp = raw_input("Rate?:")
#rate = float(inp)
#pay = hours * rate
#print "Pay:",pay,"$"

#hrs = raw_input("Enter Hours:")
#h = float(hrs)
#rate = raw_input("Enter Rate:")
#r = float(rate)
#if h <= 40.00 :
#    overpay = 0
#else :
#    overpay = h - 40
#    h = 40
#pay = h * r + overpay * r * 1.50
#print 'Pay:', pay

#try:
#    inp = raw_input("Enter Hours:")
#    h = float(inp)
#    inp = raw_input("Enter Rate:")
#    r = float(inp)
#except:
#    print "Please, enter numeric"
#    quit()
#print h, r
#if h <= 40.00 :
#    overpay = 0
#else :
#    overpay = h - 40
#h = 40
#pay = h * r + overpay * r * 1.50
#print 'Pay:', pay
