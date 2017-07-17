booleanVar=True
while booleanVar:
    try:
        number=int(raw_input("enter an integer \n> "))
        print "%o"%number
        booleanVar= False
    except ValueError:
        print "try again"

