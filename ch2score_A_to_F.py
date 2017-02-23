try:
    inp = raw_input("Enter Score:")
    sc = float(inp)
except:
    print "Please, enter numeric"
    quit()

if sc > 1.00 :
    print "Score out of range (high)"
elif sc < 0.00 : 
    print "Score out of range (low)"
elif sc >= 0.90 :
    print "U got A"
elif sc >= 0.80 :
    print "U got B"
elif sc >= 0.70 :
    print "U got C"
elif sc >= 0.60 :
    print "U got D"
else :
    print "U got F"

print "All done"