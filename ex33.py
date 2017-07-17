i=0
numbers=[]
def function(x):
    i=0
    y=int(raw_input("how much to increment?:"))
    for i in range(0,x,y):
        print "At the top i is %d"%i
        numbers.append(i)
        i=i+y
        print "Numbers now: ",numbers
        print "At the bottom i is %d"%i
#while i<6:
 #   print "At the top i is %d"%i
  #  numbers.append(i)
   # i+=1
    #print "Numbers now: ",numbers
    #print "At the bottom i is %d"%i
#print "The numbers: "
#
#for num in numbers:
 #   print num
function(100)
