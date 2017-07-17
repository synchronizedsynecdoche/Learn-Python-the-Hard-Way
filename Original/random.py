from random import *
from sys import argv
script, file_ =argv
print "This script, %s erases a file and fills it up with bottom-tier randomness" % script
file_.truncate()
numberOfLines=raw_input("how many lines?")
while true:
	file_.write(randint(0, numberOfLines))

