from sys import argv
script, filename=argv
print "we're going to erase %r" %filename
print "if you don't want that, hit ^C."
print "if you want to do that, hit ENTER"
raw_input("?")
print"opening the file..."
target=open(filename, 'w')
print("Truncating")
target.truncate()
print"now I am going to ask you for three lines."
line1=raw_input("line 1:")
line2=raw_input("line 2:")
line3=raw_input("line 3:")
print "I am going to write these to the file"
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print "And finally, we close it"
target.close()
